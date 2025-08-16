defmodule Solution do
  # 33ms - 34ms
  @spec minimum_pair_removal(nums :: [integer]) :: integer
  def minimum_pair_removal(nums) do
    minimum_pair_removal(nums, 0)
  end

  def minimum_pair_removal(nums, ans) do
    if is_sorted(nums) do
      {min_sum, min_idx} = get_min_index(nums)
      new_nums = remove_target_index(list_update_at(nums, min_idx, min_sum), min_idx + 1)
      minimum_pair_removal(new_nums, ans + 1)
    else
      ans
    end
  end

  @spec is_sorted(nums :: [integer]) :: bool
  def is_sorted([head | tail]) when tail != [] do
    if head > (tail |> hd) do
      true
    else
      is_sorted(tail)
    end
  end

  def is_sorted([_nums]) do
    false
  end

  @spec list_update_at(nums :: [integer], target :: integer, val :: integer) :: [integer]
  def list_update_at(nums, target, val) do
    Enum.reduce(nums, {0, []}, fn num, {i, res} ->
      if i == target do
        {i + 1, res ++ [val]}
      else
        {i + 1, res ++ [num]}
      end
    end) |> elem(1)
  end

  @spec get_min_index(nums :: [integer]) :: {integer, integer}
  def get_min_index(nums) do
    nums_length = Enum.count(nums)
    {_i, min_sum, min_idx} =
      Enum.reduce_while(nums, {0, 1_000_000_000_000, -1}, fn num, {i, min_sum, min_idx} ->
        if i == nums_length - 1 do
          {:halt, {i + 1, min_sum, min_idx}}
        else
          pair_sum = num + Enum.at(nums, i + 1)
          if pair_sum < min_sum do
            {:cont, {i + 1, pair_sum, i}}
          else
            {:cont, {i + 1, min_sum, min_idx}}
          end
        end
      end)
    {min_sum, min_idx}
  end

  @spec remove_target_index(nums :: [integer], target :: integer ) :: [integer]
  def remove_target_index(nums, target) do
    Enum.reduce(nums, {0, []}, fn num, {i, res} ->
      if i == target do
        {i + 1, res}
      else
        {i + 1, res ++ [num]}
      end
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_pair_removal(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
