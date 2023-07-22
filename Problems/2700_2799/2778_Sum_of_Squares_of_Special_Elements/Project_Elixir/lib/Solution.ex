defmodule Solution do
  # 343ms - 360ms
  @spec sum_of_squares(nums :: [integer]) :: integer
  def sum_of_squares(nums) do
    n = Enum.count(nums)
    Enum.reduce(1..n, 0, fn i, ans ->
      if rem(n, i) == 0 do
        num = Enum.at(nums, i - 1)
        ans + num*num
      else
        ans
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sum_of_squares(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
