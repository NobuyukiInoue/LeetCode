defmodule Solution do
  # 518ms - 587ms
  @spec the_maximum_achievable_x(num :: integer, t :: integer) :: integer
  def the_maximum_achievable_x(num, t) do
    num + 2*t
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    num = Enum.at(flds, 0) |> String.to_integer()
    t = Enum.at(flds, 1) |> String.to_integer()
    "num = " <> Integer.to_string(num) <> ", t = " <> Integer.to_string(t) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.the_maximum_achievable_x(num, t)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
