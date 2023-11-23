defmodule Solution do
  # 4762ms - 4775ms
  @spec circular_array_loop(nums :: [integer]) :: boolean
  def circular_array_loop(nums) do
    n = Enum.count(nums)
    visited = [for _ <- 0..n-1 do False end]
    Enum.reduce_while(nums, {0, visited, false}, fn num, {i, visited, _} ->
      if Enum.at(visited, i) do
        {:cont, {i + 1, visited, false}}
      else
        {visited, res} = loop_visited(nums, n, visited, Map.new(), i, num, num >= 0)
        if res do
          {:halt, {i + 1, visited, true}}
        else
          {:cont, {i + 1, visited, false}}
        end
      end
    end) |> elem(2)
  end

  @spec loop_visited(nums :: [integer], n :: integer, visited :: [bool], dic :: %{}, index :: integer, num :: integer, forward :: boolean) :: {[bool], boolean}
  def loop_visited(nums, n, visited, dic, index, num, forward) do
    visited = List.replace_at(visited, index, true)
    newIndex = rem(index + num, n)
    newIndex = if newIndex < 0 do; newIndex + n else newIndex end
    newNum = Enum.at(nums, newIndex)
    if index == newIndex or forward != (newNum >= 0) do
      {visited, false}
    else
      if Map.has_key?(dic, index) do
        {visited, true}
      else
        loop_visited(nums, n, visited, Map.put(dic, index, true), newIndex, newNum, forward)
      end
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
      result = Solution.circular_array_loop(nums)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
