defmodule Solution do
  # 389ms - 425ms
  @spec max_sub_array(nums :: [integer]) :: integer
  def max_sub_array(nums) do
    Enum.reduce(nums, {-1_00001, 0}, fn num, {max_sum, current_sum} ->
      current_sum = current_sum + num
      max_sum =
      if current_sum > max_sum do
        current_sum
      else
        max_sum
      end
      if current_sum < 0 do
        {max_sum, 0}
      else
        {max_sum, current_sum}
      end
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, ",")

    nums = for n <- flds, do: n |> String.trim() |> String.to_integer()
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_sub_array(nums)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
