defmodule Solution do
  # 314ms - 322ms
  @spec longest_monotonic_subarray(nums :: [integer]) :: integer
  def longest_monotonic_subarray(nums) do
    Enum.reduce(nums, {nums |> hd, 1, 1, 1}, fn num, {prev, incr, decr, ans} ->
      incr = if num > prev do; incr + 1 else 1 end
      decr = if num < prev do; decr + 1 else 1 end
      {num, incr, decr, Enum.max([ans, incr, decr])}
    end)
    |> elem(3)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.longest_monotonic_subarray(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
