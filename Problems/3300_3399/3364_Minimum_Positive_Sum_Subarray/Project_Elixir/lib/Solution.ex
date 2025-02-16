defmodule Solution do
  # 5ms
  @spec minimum_sum_subarray(nums :: [integer], l :: integer, r :: integer) :: integer
  def minimum_sum_subarray(nums, l, r) do
    res = do_minimum_sum_subarray(nums, l, r, nil)
    if res && res > 0, do: res, else: -1
  end

  defp do_minimum_sum_subarray([], _l, _r, res), do: res
  defp do_minimum_sum_subarray(nums, l, r, res) do
    res = min(res, count_min_sum(nums, l, r, 0, 0, res))
    do_minimum_sum_subarray(tl(nums), l, r, res)
  end

  defp count_min_sum([], _l, _r, _sum, _count, res), do: res
  defp count_min_sum([n | tl], l, r, sum, count, res) do
    count = count + 1
    sum = sum + n
    cond do
      count < l -> count_min_sum(tl, l, r, sum, count, res)
      count > r -> res
      sum < 1 -> count_min_sum(tl, l, r, sum, count, res)
      true -> count_min_sum(tl, l, r, sum, count, min(res, sum))
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
