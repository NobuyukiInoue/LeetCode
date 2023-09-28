defmodule Solution do
  # 247ms - 330ms
  @spec minimum_right_shifts(nums :: [integer]) :: integer
  def minimum_right_shifts(nums) do
    {_, _, pos, ind} = Enum.reduce(nums, {0, nums |> hd, 0, 0}, fn num, {i, prev, pos, ind} ->
      if prev > num do
        {i + 1, num, pos + 1, i}
      else
        {i + 1, num, pos, ind}
      end
    end)
    n = Enum.count(nums)
    cond do
      pos > 1 ->
        -1
      ind == 0 ->
        0
      Enum.at(nums, n - 1) > nums |> hd ->
        -1
      True ->
        n - ind
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_right_shifts(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
