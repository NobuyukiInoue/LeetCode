defmodule Solution do
  # 2926ms - 2951ms
  @spec three_sum(nums :: [integer]) :: [[integer]]
  def three_sum(nums) do
    l = length(nums) - 1

    freq =
      nums
      |> Enum.frequencies()

    map =
      nums
      |> Enum.with_index()
      |> Enum.group_by(fn {v, _} -> v end, fn {_, i} -> i end)

    tuple =
      nums
      |> List.to_tuple()

    Stream.unfold({0, 1}, fn {i, j} ->
      if j < l, do: {{i, j}, {i, j + 1}}, else: {{i, j}, {i+1, i+2}}
    end)
    |> Stream.take_while(fn {i, _} -> i < l end)
    |> Stream.map(fn {i, j} ->
      a = elem(tuple, i)
      b = elem(tuple, j)

      c =  -1 * (a + b)
      case Map.get(freq, c) do
        nil -> nil
        count when count >= 3 -> [a, b, c] |> Enum.sort()
        _ ->
          case Map.get(map, c) |> Enum.filter(& &1 != i && &1 != j) do
            [] -> nil
            _ -> [a, b, c] |> Enum.sort()
          end
      end
    end)
    |> Stream.reject(& &1 == nil)
    |> Stream.uniq()
    |> Enum.to_list()
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
      result = Solution.three_sum(nums)
      "result = " <> Mylib.intIntList_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
    :ok
  end
end
