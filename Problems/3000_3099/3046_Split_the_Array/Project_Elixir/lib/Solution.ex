defmodule Solution do
  # 316ms - 336ms
  @spec is_possible_to_split(nums :: [integer]) :: boolean
  def is_possible_to_split(nums) do
    Enum.reduce_while(nums, {%{}, false}, fn num, {cnts, _ans} ->
      cnts = Map.put(cnts, num, Map.get(cnts, num, 0) + 1)
      if cnts[num] == 3 do
        {:halt, {cnts, false}}
      else
        {:cont, {cnts, true}}
      end
    end)
    |> elem(1)
  end

  # 337ms - 346ms
  @spec is_possible_to_split2(nums :: [integer]) :: boolean
  def is_possible_to_split2(nums) do
    cnts = Enum.reduce(nums, %{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)
    Enum.all?(Map.values(cnts), fn x -> x < 3 end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_possible_to_split(nums)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
