defmodule Solution do
  # 249ms - 303ms
  @spec delete_greatest_value(grid :: [[integer]]) :: integer
  def delete_greatest_value(grid) do
    s_grid =
      Enum.reduce(grid, [], fn row, s_grid ->
        [Enum.sort(row)] ++ s_grid
      end)
    Enum.reduce(s_grid, %{}, fn row, col_max ->
      Enum.reduce(row, {0, col_max}, fn col, {j, col_max} ->
        {j + 1, Map.put(col_max, j, max(Map.get(col_max, j, 0), col))}
      end)
      |> elem(1)
    end)
    |> Map.values()
    |> Enum.sum()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    flds = String.split(temp, "],[")

    grid =
    for row <- flds do
      for col <- String.split(row, ",") do
        String.to_integer(col)
      end
    end

    "grid = [" <> Mylib.intIntList_to_string(grid) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.delete_greatest_value(grid)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
