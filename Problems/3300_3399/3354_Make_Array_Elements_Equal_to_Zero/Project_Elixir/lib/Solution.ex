defmodule Solution do
  # 3ms
  @spec count_valid_selections(nums :: [integer]) :: integer
  def count_valid_selections(nums) do
    {index, left} =
      Enum.reduce_while(nums, {0, 0}, fn num, {i, left} ->
        if num == 0 do
          {:halt, {i, left}}
        else
          {:cont, {i + 1, left + num}}
        end
      end)

    nums_right = Enum.slice(nums, index, Enum.count(nums))
    {_i, right} =
      Enum.reduce(nums_right, {0, 0}, fn num, {i, right} ->
        {i + 1, right + num}
      end)

    {_i, _left, _right, count} =
      Enum.reduce(nums_right, {0, left, right, 0}, fn num, {i, left, right, count} ->
        cond do
          num != 0 ->
            {i + 1, left + num, right - num, count}
          left == right ->
            {i + 1, left + num, right - num, count + 2}
          left - 1 == right || left + 1 == right ->
            {i + 1, left + num, right - num, count + 1}
          true ->
            {i + 1, left + num, right - num, count}
        end
      end)
    count
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_valid_selections(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
