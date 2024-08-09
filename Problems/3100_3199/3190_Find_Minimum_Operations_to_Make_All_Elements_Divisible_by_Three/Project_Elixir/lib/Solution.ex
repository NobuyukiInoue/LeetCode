defmodule Solution do
  # 290ms - 318ms
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    Enum.count(nums, fn n -> rem(n, 3) != 0 end)
  end

  # 264ms - 307ms
  @spec minimum_operations2(nums :: [integer]) :: integer
  def minimum_operations2(nums) do
    nums
    |> Enum.filter(fn num -> rem(num, 3) != 0 end)
    |> Enum.count()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_operations(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
