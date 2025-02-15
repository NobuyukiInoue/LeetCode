defmodule Solution do
  # 2ms
  @spec has_increasing_subarrays(nums :: [integer], k :: integer) :: boolean
  def has_increasing_subarrays(nums, k) do
    count_increasing_subarrays(nums |> tl, nums |> hd, 1, 0, 0) >= k
  end

  @spec count_increasing_subarrays(nums :: [integer], prev :: integer, cnt :: integer, pre_max_cnt :: integer, res :: integer) :: integer
  def count_increasing_subarrays(nums, _prev, _cnt, _pre_max_cnt, res) when nums == [] do
    res
  end

  def count_increasing_subarrays(nums, prev, cnt, pre_max_cnt, res) do
    num = nums |> hd
    {cnt, pre_max_cnt} =
      if num > prev do
        {cnt + 1, pre_max_cnt}
      else
        {1, cnt}
      end
    count_increasing_subarrays(nums |> tl, num, cnt, pre_max_cnt, Enum.max([res, div(cnt, 2), min(pre_max_cnt, cnt)]))
  end

  def debug(nums, prev, cnt, pre_max_cnt, res) do
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()
    "prev = " <> Integer.to_string(prev) <> ", cnt = " <> Integer.to_string(cnt) <> ", pre_max_cnt = " <> Integer.to_string(pre_max_cnt) <> ", res = " <> Integer.to_string(res) |> IO.puts()
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

    k = String.to_integer(Enum.at(flds, 1))
    "nums = [" <> Mylib.intList_to_string(nums) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.has_increasing_subarrays(nums, k)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
