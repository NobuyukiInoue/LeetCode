defmodule Solution do
  # 299ms - 351ms
  @spec sum_of_multiples(n :: integer) :: integer
  def sum_of_multiples(n) do
    Enum.reduce(1..n, 0, fn i, acc ->
      if rem(i, 3) == 0 or rem(i, 5) == 0 or rem(i, 7) == 0 do
        i + acc
      else
        acc
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")
    n = String.to_integer(flds)
    "n = " <> to_string(n) |> IO.puts()

    execright = Benchmark.measure(fn ->
      result = Solution.sum_of_multiples(n)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(execright, 3)) <> " [s]\n" |> IO.puts()
  end
end
