defmodule Solution2 do
  # 47ms
  @spec minimum_sum_subarray(nums :: [integer], l :: integer, r :: integer) :: integer
  def minimum_sum_subarray(nums, l, r) do
    min_sum = minimum_sum_subarray(nums, l, r, Enum.count(nums), 1_000_000_000)
    if min_sum == 1_000_000_000 do; -1 else min_sum end
  end

  @spec minimum_sum_subarray(nums :: [integer], length :: integer, r :: integer, n :: integer, min_sum :: integer) :: integer
  def minimum_sum_subarray(_nums, length, r, _n, min_sum) when length > r do
    min_sum
  end

  def minimum_sum_subarray(nums, length, r, n, min_sum) when length > n do
    minimum_sum_subarray(nums, length + 1, r, n, min_sum)
  end

  def minimum_sum_subarray(nums, length, r, n, min_sum) do
    window_sum = Enum.sum(Enum.slice(nums, 0, length))
    min_sum = if window_sum > 0 do; min(min_sum, window_sum) else min_sum end
    if length >= n do
      min_sum = if window_sum > 0 do; min(min_sum, window_sum) else min_sum end
      minimum_sum_subarray(nums, length + 1, r, n, min_sum)
    else
      min_sum = Enum.reduce(length..n-1, {min_sum, window_sum}, fn i, {min_sum, window_sum} ->
        window_sum = window_sum + Enum.at(nums, i) - Enum.at(nums, i - length)
        min_sum = if window_sum > 0 do; min(min_sum, window_sum) else min_sum end
        {min_sum, window_sum}
      end) |> elem(0)
      minimum_sum_subarray(nums, length + 1, r, n, min_sum)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums =
      for num <- String.split(Enum.at(flds, 0), ",") do
          String.to_integer(num)
      end

    l = String.to_integer(Enum.at(flds, 1))
    r = String.to_integer(Enum.at(flds, 2))
    "nums = [" <> Mylib.intList_to_string(nums) <> "], l = " <> Integer.to_string(l) <> ", r = " <> Integer.to_string(r) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_sum_subarray(nums, l, r)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
