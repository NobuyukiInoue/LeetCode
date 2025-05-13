defmodule Solution do
  # 2ms - 3ms
  @spec count_partitions(nums :: [integer]) :: integer
  def count_partitions(nums) do
    n = Enum.count(nums)
    Enum.reduce_while(nums, {0, Enum.sum(nums), 0, 0}, fn num, {i, sum_l, sum_r, ans} ->
      if i == n - 1 do
        {:halt, {i, sum_l, sum_r, ans}}
      else
        {sum_l, sum_r} = {sum_l - num, sum_r + num}
        if rem(sum_l - sum_r, 2) == 0 do
          {:cont, {i + 1, sum_l, sum_r, ans + 1}}
        else
          {:cont, {i + 1, sum_l, sum_r, ans}}
        end
      end
    end) |> elem(3)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_partitions(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
