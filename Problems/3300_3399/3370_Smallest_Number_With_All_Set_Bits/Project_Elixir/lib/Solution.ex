defmodule Solution do
  # 0ms
  @spec smallest_number(n :: integer) :: integer
  def smallest_number(n) do
    smallest_number(n, 1)
  end

  @spec smallest_number(n :: integer, cur :: integer) :: integer
  def smallest_number(n, cur) when cur - 1 < n do
    smallest_number(n, cur*2)
  end

  def smallest_number(_n, cur) do
    cur - 1
  end

  @spec loop_main(temp :: String.t) :: :ox
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")

    n = String.to_integer(flds)
    "n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.smallest_number(n)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
