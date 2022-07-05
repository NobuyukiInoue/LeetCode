defmodule Solution do
  # 402ms - 452ms
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    check(nums, 0, %{}, target)
  end

  def check([h|_t], count, map, target) when is_map_key(map, target-h) do
    [map[target-h], count]
  end

  def check([h|t], count, map, target) do
    check(t, count+1, Map.put(map, h, count), target)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")
    flds0 = String.split(Enum.at(flds, 0), ",")

    nums = for n <- flds0, do: n |> String.trim() |> String.to_integer()
    target = Enum.at(flds, 1) |> String.to_integer()
    "nums = [" <> Mylib.intList_to_string(nums) <> "], target = " <> Integer.to_string(target) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.two_sum(nums, target)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
