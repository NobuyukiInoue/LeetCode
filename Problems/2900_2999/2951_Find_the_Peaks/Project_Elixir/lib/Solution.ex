# 255ms - 300ms
defmodule Solution do
  @spec find_peaks(mountain :: [integer]) :: [integer]
  def find_peaks(mountain) do
    n = mountain |> Enum.count()
    map = Enum.reduce(mountain, {0, Map.new()}, fn cur, {i, map} ->
      {i + 1, Map.put(map, i, cur)}
    end) |> elem(1)
    find_peaks(map, n)
  end

  @spec find_peaks(map :: %{}, n :: integer) :: [integer]
  def find_peaks(_map, n) when n < 2 do
    []
  end

  def find_peaks(map, n) do
    Enum.reduce(1..n-2, [], fn i, res ->
      if map[i - 1] < map[i] and map[i] > map[i + 1] do
        [i] ++ res
      else
        res
      end
    end) |> Enum.reverse()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    mountain = for n <- String.split(flds, ",") do String.to_integer(n) end
    "mountain = [" <> Mylib.intList_to_string(mountain) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_peaks(mountain)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
