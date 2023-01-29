defmodule Solution do
  # 331ms - 362ms
  @spec distinct_integers(n :: integer) :: integer
  def distinct_integers(n) when n - 1 > 1 do
    n - 1
  end

  def distinct_integers(_) do
    1
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    n = String.to_integer(flds)
    "n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.distinct_integers(n)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
