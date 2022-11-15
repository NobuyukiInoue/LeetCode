defmodule Solution do
  # 607ms - 624ms
  @spec max_area(height :: [integer]) :: integer
  def max_area(height) do
    find_max_area(height, Enum.reverse(height), length(height)-1, 0)
  end

  def find_max_area(_hts, _rev_hts, 0, max), do: max
  def find_max_area([ht | _hts] = heights, [rht | rhts], length, max) when ht > rht do
    find_max_area(heights, rhts, length - 1, max(max, rht * length))
  end
  def find_max_area([ht | hts], [rht | _rhts] = r_heights, length, max) when ht <= rht do
    find_max_area(hts, r_heights, length - 1, max(max, ht * length))
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, ",")

    height = for n <- flds, do: n |> String.trim() |> String.to_integer()
    "height = [" <> Mylib.intList_to_string(height) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_area(height)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
