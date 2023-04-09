defmodule Solution do
  # 209ms - 227ms
  @spec pass_the_pillow(n :: integer, time :: integer) :: integer
  def pass_the_pillow(n, time) do
    n - abs(n - 1 - rem(time, (n * 2 - 2)))
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    n = Enum.at(flds, 0) |> String.to_integer()
    time = Enum.at(flds, 1) |> String.to_integer()
    "n = " <> Integer.to_string(n) <> ", time = " <> Integer.to_string(time) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.pass_the_pillow(n, time)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
