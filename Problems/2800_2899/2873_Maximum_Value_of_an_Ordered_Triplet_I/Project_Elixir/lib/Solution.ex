defmodule Solution do
  # 277ms - 288ms
  @spec maximum_triplet_value(nums :: [integer]) :: integer
  def maximum_triplet_value(nums) do
    Enum.reduce(nums, {0, 0, 0}, fn num, {res, maxa, maxab} ->
      {max(res, maxab*num), max(maxa, num), max(maxab, maxa - num)}
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.maximum_triplet_value(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
