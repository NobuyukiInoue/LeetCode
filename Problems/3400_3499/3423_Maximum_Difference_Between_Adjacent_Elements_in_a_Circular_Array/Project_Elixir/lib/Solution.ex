defmodule Solution do
  # 3ms
  @spec max_adjacent_distance(nums :: [integer]) :: integer
  def max_adjacent_distance(nums) do
    n = Enum.count(nums)
    Enum.reduce(nums, {0, 0}, fn num, {i, ans} ->
      next_i = rem(i + 1, n)
      {i + 1, max(ans, abs(num - Enum.at(nums, next_i)))}
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
      result = Solution.max_adjacent_distance(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
