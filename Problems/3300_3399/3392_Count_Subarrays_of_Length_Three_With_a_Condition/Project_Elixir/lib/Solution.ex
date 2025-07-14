defmodule Solution do
  # 25ms - 28ms
  @spec count_subarrays(nums :: [integer]) :: integer
  def count_subarrays(nums) do
    n = Enum.count(nums)
    Enum.reduce_while(nums, {0, 0}, fn num, {i, ans} ->
      cond do
        i == n - 2->
          {:halt, {i + 1, ans}}
        Enum.at(nums, i + 1) == (num + Enum.at(nums, i + 2))*2 ->
          {:cont, {i + 1, ans + 1}}
        true ->
          {:cont, {i + 1, ans}}
      end
    end) |> elem(1)
  end

  # 17ms - 29ms
  @spec count_subarrays2(nums :: [integer]) :: integer
  def count_subarrays2(nums) do
      nums
    |> Enum.chunk_every(3, 1, :discard)
    |> Enum.count(fn [a, b, c] -> rem(b, 2) == 0 and a + c == div(b, 2) end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_subarrays(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
