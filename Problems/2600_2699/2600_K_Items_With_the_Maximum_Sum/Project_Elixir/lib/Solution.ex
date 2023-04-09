defmodule Solution do
  # 433ms - 434ms
  @spec k_items_with_maximum_sum(num_ones :: integer, num_zeros :: integer, num_neg_ones :: integer, k :: integer) :: integer
  def k_items_with_maximum_sum(num_ones, num_zeros, num_neg_ones, k) do
    Enum.min([k, num_ones]) - Enum.max([0, k - num_zeros - num_ones])
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    num_ones = Enum.at(flds, 0) |> String.to_integer()
    num_zeros = Enum.at(flds, 1) |> String.to_integer()
    num_neg_ones = Enum.at(flds, 2) |> String.to_integer()
    k = Enum.at(flds, 3) |> String.to_integer()

    "num_ones = " <> Integer.to_string(num_ones) <>
    ", num_ones num_zeros = " <> Integer.to_string(num_zeros) <>
    ", num_neg_ones = " <> Integer.to_string(num_neg_ones) <>
    ", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.k_items_with_maximum_sum(num_ones, num_zeros, num_neg_ones, k)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
