defmodule Solution do
  # 278ms - 331ms
  @spec count_and_say(n :: integer) :: String.t
  def count_and_say(1), do: "1"
  def count_and_say(n) do
    Enum.reduce(2..n, count_and_say(1), fn _, s ->
      countAndSay(s)
    end)
  end

  def countAndSay(n) do
    String.graphemes(n)
    |> Enum.reduce({"", []}, fn
      s, {"", []} -> {s, [{1, s}]}
      s, {char, [{cpt,_} | t]} when s == char -> {char, [{cpt + 1, char} | t]}
      s, {_, list} -> {s, [{1, s} | list]}
    end)
    |> elem(1)
    |> Enum.reverse
    |> Enum.map(fn {cpt, c} -> "#{cpt}" <> c end)
    |> Enum.join("")
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    n = temp |> String.to_integer()
    "n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_and_say(n)
      "result = \"" <> result <> "\"" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
