defmodule Solution do
  # 2ms
  @spec construct_transformed_array(nums :: [integer]) :: [integer]
  def construct_transformed_array(nums) do
    n = Enum.count(nums)
    Enum.reduce(nums, {0, []}, fn num, {i, ans} ->
      {i + 1, [Enum.at(nums, rem(i + rem(num, n) + n, n))] ++ ans}
    end)
    |> elem(1)
    |> Enum.reverse()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.construct_transformed_array(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
