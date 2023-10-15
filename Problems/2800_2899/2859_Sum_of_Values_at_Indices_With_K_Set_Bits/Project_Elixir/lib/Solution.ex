defmodule Solution do
  # 308ms - 315ms
  @spec sum_indices_with_k_set_bits(nums :: [integer], k :: integer) :: integer
  def sum_indices_with_k_set_bits(nums, k) do
    Enum.reduce(nums, {0, 0}, fn num, {i, total} ->
      if bit_count(i, 0) == k do
        {i + 1, total + num}
      else
        {i + 1, total}
      end
    end) |> elem(1)
  end

  @spec bit_count(k :: integer, count :: integer) :: integer
  def bit_count(k, count) when k != 0 do
    if Bitwise.band(k, 0x01) != 0 do
      bit_count(Bitwise.>>>(k, 1), count + 1)
    else
      bit_count(Bitwise.>>>(k, 1), count)
    end
  end

  def bit_count(_k, count) do
    count
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()
    "nums = [" <>  Mylib.intList_to_string(nums) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sum_indices_with_k_set_bits(nums, k)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
