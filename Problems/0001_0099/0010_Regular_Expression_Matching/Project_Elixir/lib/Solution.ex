require String
require Agent

defmodule Solution do
  # Wrong Answer
  @spec is_match(s :: String.t, p :: String.t) :: boolean
  def is_match(s, p) do
    start()
    sGraphemes = String.graphemes(s)
    pTokens = String.graphemes(p) |> tokenize
    match(sGraphemes, pTokens)
  end

  def start do
    Agent.start_link(fn -> %{} end, name: MODULE)
  end

  @spec match(any, any) :: any
  def match(graphemes, tokens) do
    cached_value = Agent.get(MODULE, &(Map.get(&1, [graphemes, tokens], nil)))
    if cached_value == nil do
      res = case [graphemes, tokens] do
        [[], []] -> true
        [[], [[Char]]] -> true
        [[], [[Char] | tail]] -> match([], tail)
        [[Char], [["."]]] -> true
        [[Char], ["."]] -> true
        [[Char], [[Char]]] -> true
        [[Char], [Char]] -> true
        [[Char | t1], [[char] | t2]] -> cond do
          match([char | t1], t2) -> true
          match(t1, t2) -> true
          match(t1, [[char] | t2]) -> true
          true -> false
        end

        [[char | t1], [["."] | t2]] -> cond do
          match([char | t1], t2) -> true
          match(t1, t2) -> true
          match(t1, [["."] | t2]) -> true
          true -> false
        end
        [[Char | t1], [[Other] | t2]] -> match([Char | t1], t2)
        [[Char | t1], [Char | t2]] -> cond do
          match(t1, t2) -> true
          true -> false
        end

        [[Char | t1], ["." | t2]] -> cond do
          match(t1, t2) -> true
          true -> false
        end
        _ -> false
      end
      Agent.update(MODULE, &(Map.put(&1, [graphemes, tokens], res)))
      res
    else
      cached_value
    end
  end

  def tokenize(graphemes) do
    case graphemes do
      [] -> []
      [head] -> [head]
      [head | [next | tail]] -> cond do
        next == "*" -> [[head] | tokenize(tail)]
        true -> [head | tokenize([next | tail])]
      end
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, ",")
    s = Enum.at(flds, 0)
    p = Enum.at(flds, 1)
    "s = " <> s <> ", p = " <> p |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_match(s, p)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
