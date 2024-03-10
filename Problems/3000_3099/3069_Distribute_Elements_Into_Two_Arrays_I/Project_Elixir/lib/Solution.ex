defmodule Solution do
  # 290ms - 327ms
  @spec result_array(nums :: [integer]) :: [integer]
  def result_array(nums) do
    [num1 | [num2 | tail]] = nums
    {arr1, arr2} =
      Enum.reduce(tail, {[num1], [num2]}, fn num, {arr1, arr2} ->
        if arr1 |> hd > arr2 |> hd do
          {[num] ++ arr1, arr2}
        else
          {arr1, [num] ++ arr2}
        end
      end)
    (arr1 |> Enum.reverse()) ++ (arr2 |> Enum.reverse())
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.result_array(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
