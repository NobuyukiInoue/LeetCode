defmodule Solution do
  # 885ms - 1014ms
  @spec longest_square_streak(nums :: [integer]) :: integer
  def longest_square_streak(nums) do
    longest_square_streak(Enum.sort(nums), Enum.reduce(nums, %{}, fn x, acc -> Map.update(acc, x, 0, &(&1 + 1)) end), 1)
  end

  @spec longest_square_streak(nums :: [integer], map :: {integer, integer}, ans :: integer) :: integer
  def longest_square_streak([], _, ans) when ans == 1 do
    -1
  end

  def longest_square_streak([], _, ans) do
    ans
  end

  def longest_square_streak([head | tail], map, ans) do
    sqrt = trunc(:math.sqrt(head))
#   "head = " <> Integer.to_string(head) <> ", sqrt = " <> Integer.to_string(sqrt) |> IO.puts()
#   "map = " <> Mylib.intList_to_string(Map.values(map)) |> IO.puts()
    if sqrt*sqrt == head do
#     "  sqrt*sqrt == head" |> IO.puts()
      new_map = Map.put(map, head, Map.get(map, sqrt, 0) + 1)
#     "  new_map = " <> Mylib.intList_to_string(Map.values(new_map)) |> IO.puts()
      if Map.get(new_map, head) > ans do
        longest_square_streak(tail, new_map, Map.get(new_map, head))
      else
        longest_square_streak(tail, new_map, ans)
      end
    else
      longest_square_streak(tail, Map.put(map, head, 1), ans)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.longest_square_streak(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
