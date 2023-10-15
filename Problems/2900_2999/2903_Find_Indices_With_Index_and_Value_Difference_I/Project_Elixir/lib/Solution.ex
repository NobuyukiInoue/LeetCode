defmodule Solution do
  # 278ms - 319ms
  @spec find_indices(nums :: [integer], index_difference :: integer, value_difference :: integer) :: [integer]
  def find_indices(nums, index_difference, value_difference) do
    len_nums = Enum.count(nums)
    if index_difference >= len_nums do
      if value_difference == 0 and index_difference == 0 do
        [0, 0]
      else
        [-1, -1]
      end
    else
      Enum.reduce_while(index_difference..len_nums-1, {0, 0, [-1, -1]}, fn i, {min_i, max_i, ans} ->
        min_i =
          if Enum.at(nums, i - index_difference) < Enum.at(nums, min_i) do
            i - index_difference
          else
            min_i
          end
        max_i =
          if Enum.at(nums, i-index_difference) > Enum.at(nums, max_i) do
            i - index_difference
          else
            max_i
          end
        cond do
          Enum.at(nums, i) - Enum.at(nums, min_i) >= value_difference ->
            {:halt, {min_i, max_i, [min_i, i]}}
          Enum.at(nums, max_i) - Enum.at(nums, i) >= value_difference ->
            {:halt, {min_i, max_i, [max_i, i]}}
          true ->
            {:cont, {min_i, max_i, ans}}
        end
      end) |> elem(2)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    index_difference = Enum.at(flds, 1) |> String.to_integer()
    value_difference = Enum.at(flds, 2) |> String.to_integer()
    "nums = [" <>  Mylib.intList_to_string(nums) <> "], index_difference = " <> Integer.to_string(index_difference) <> ", value_difference = " <> Integer.to_string(value_difference) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_indices(nums, index_difference, value_difference)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
