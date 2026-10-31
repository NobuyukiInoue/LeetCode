defmodule Solution do
  # 2ms
  @spec alternating_sum(nums :: [integer]) :: integer
  def alternating_sum(nums) do
    nums
    |> Enum.with_index()
    |> Enum.reduce(0, fn
      {num, i}, acc when rem(i, 2) == 0 -> acc + num
      {num, i}, acc -> acc - num
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
      result = Solution.alternating_sum(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
