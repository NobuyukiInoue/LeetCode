defmodule Solution do
  # 266ms - 281ms
  @spec smallest_range_ii(nums :: [integer], k :: integer) :: integer
  def smallest_range_ii(nums, k) do
    smallest_range_ii(Enum.sort(nums), k, Enum.count(nums))
  end

  @spec smallest_range_ii(nums :: [integer], k :: integer, n :: integer) :: integer
  def smallest_range_ii(_nums, _k, n) when n <= 1 do
    0
  end

  def smallest_range_ii(nums, k, n) when n <= 2 do
    score = List.last(nums) - (nums |> hd)
    res = score
    v_max = max(Enum.at(nums, 0) + k, Enum.at(nums, 1) - k)
    v_min = min(Enum.at(nums, 1) - k, Enum.at(nums, 0) + k)
    score = v_max - v_min
    min(res, score)
  end

  def smallest_range_ii(nums, k, n) do
    nums_head = nums |> hd
    nums_last = List.last(nums)
    score = nums_last - nums_head
    helper(0, nums, k, n, score, nums_head, nums_last)
  end

  # 266ms - 281ms
  @spec helper(i :: integer, nums :: [integer], k :: integer, n :: integer, res :: integer, nums_head :: integer, nums_last :: integer) :: integer
  def helper(i, [_head | _tail], _k, n, res, _nums_head, _nums_last) when i == n - 1 do
    res
  end

  def helper(i, [head | tail], k, n, res, nums_head, nums_last) do
    v_max = max(head + k, nums_last - k)
    v_min = min((tail |> hd) - k, nums_head + k)
    score = v_max - v_min
    helper(i + 1, tail, k, n, min(res, score), nums_head, nums_last)
  end

  # 1072ms - 1189ms
  def smallest_range_ii_slow1(nums, k, n) do
    nums_head = nums |> hd
    nums_last = List.last(nums)
    score = nums_last - (nums |> hd)
    Enum.reduce(0..n-2, {0, 0, score, score}, fn i, {_v_max, _v_min, _score, res} ->
      v_max = max(Enum.at(nums, i) + k, nums_last - k)
      v_min = min(Enum.at(nums, i + 1) - k, nums_head + k)
      score = v_max - v_min
      {v_max, v_min, score, min(res, score)}
    end) |> elem(3)
  end

  # 2122ms - 2153ms
  def smallest_range_ii_slow2(nums, k, n) do
    score = List.last(nums) - (nums |> hd)
    Enum.reduce(0..n-2, {0, 0, score, score}, fn i, {_v_max, _v_min, _score, res} ->
      v_max = max(Enum.at(nums, i) + k, Enum.at(nums, n-1) - k)
      v_min = min(Enum.at(nums, i + 1) - k, Enum.at(nums, 0) + k)
      score = v_max - v_min
      {v_max, v_min, score, min(res, score)}
    end) |> elem(3)
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
      result = Solution.smallest_range_ii(nums, k)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
