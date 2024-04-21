defmodule Solution do
  # 658ms - 696ms
  @spec count_alternating_subarrays(nums :: [integer]) :: integer
  def count_alternating_subarrays(nums) do
    Enum.reduce(nums |> tl, {nums |> hd, 1, 1}, fn num, {prev, size, ans} ->
      if prev == num do
        {num, 1, ans + 1}
      else
        {num, size + 1, ans + size + 1}
      end
    end)
    |> elem(2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_alternating_subarrays(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
