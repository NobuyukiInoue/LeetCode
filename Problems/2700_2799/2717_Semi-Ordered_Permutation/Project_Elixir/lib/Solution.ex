defmodule Solution do
  # 381ms - 422ms
  @spec semi_ordered_permutation(nums :: [integer]) :: integer
  def semi_ordered_permutation(nums) do
    n = Enum.count(nums)
    {_, {pos1, pos2}} =
      Enum.reduce(nums, {0, {0, 0}}, fn num, {i, {pos1, pos2}} ->
        cond do
          num == 1 ->
            {i + 1, {i, pos2}}
          num == n ->
            {i + 1, {pos1, i}}
          true ->
            {i + 1, {pos1, pos2}}
        end
      end)
    if pos1 > pos2, do: pos1 + n - 1 - pos2 - 1, else: pos1 + n - 1 - pos2
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.semi_ordered_permutation(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
