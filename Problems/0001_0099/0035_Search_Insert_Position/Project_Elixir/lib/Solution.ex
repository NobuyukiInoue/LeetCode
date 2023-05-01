defmodule Solution do
  # 240ms - 254ms
  @spec search_insert(nums :: [integer], target :: integer) :: integer
  def search_insert(nums, target) do
    nums |>
    Enum.reduce({nil, 0}, fn num, {_, i} ->
      if target <= num do
        {:halt, i}
      else
        {:cont, i + 1}
      end
    end) |> elem(1)
  end

  # 249ms - 263ms
  def search_insert_use_find_index(nums, target) do
    i = Enum.find_index(nums, fn x -> x >= target end)
    if i == nil do
      Enum.count(nums)
    else
      i
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    target = Enum.at(flds, 1) |> String.to_integer()
    "flds = [" <>  Mylib.intList_to_string(nums) <> "], target = " <> Integer.to_string(target) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.search_insert(nums, target)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
