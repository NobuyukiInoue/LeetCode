defmodule Solution_bad do
  # Time Limite Exceeded 29/30
  @spec count_and_say(n :: integer) :: String.t
  def count_and_say(n) when n == 1 do
    "1"
  end

  def count_and_say(n) do
    loop_right(n, "", count_and_say(n - 1), 0, 0)
  end

  def loop_right(n, ans, res, left, right) do
    if right == String.length(res) do
      ans
    else
      {counter, right} = get_right(n, res, 0, left, right)
      loop_right(n, ans <> Integer.to_string(counter) <> String.at(res, left), res, right, right)
    end
  end

  @spec get_right(n :: integer, res :: String.t, counter :: integer, left :: integer, right :: integer) :: {integer, integer}
  def get_right(n, res, counter, left, right) do
    if String.at(res, left) != String.at(res, right) or right == String.length(res) do
      {counter, right}
    else
      get_right(n, res, counter + 1, left, right + 1)
    end
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
