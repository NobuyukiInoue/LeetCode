defmodule Solution do
  # 9ms - 22ms
  @spec subarray_sum(nums :: [integer]) :: integer
  def subarray_sum(nums) do
    Enum.reduce(nums, {0, 0}, fn num, {i, ans} ->
      start = max(0, i - num)
      {i + 1, ans + Enum.sum(Enum.slice(nums, start, i + 1 - start))}
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
      result = Solution.subarray_sum(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
