defmodule Solution do
  # 332ms - 336ms
  @spec modified_matrix(matrix :: [[integer]]) :: [[integer]]
  def modified_matrix(matrix) do
    max_col =
      Enum.reduce(matrix, %{}, fn row, max_col ->
        Enum.reduce(row, {0, max_col}, fn col, {j, max_col} ->
          {j + 1, Map.put(max_col, j, max(Map.get(max_col, j, 0), col))}
        end) |> elem(1)
      end)

    Enum.reduce(matrix, [], fn row, new_rows ->
      cols =
        Enum.reduce(row, {0, []}, fn col, {j, new_cols} ->
          if col == -1 do
            {j + 1, [max_col[j]] ++ new_cols}
          else
            {j + 1, [col] ++ new_cols}
          end
        end)
        |> elem(1)
        |> Enum.reverse()
      [cols] ++ new_rows
    end)
    |> Enum.reverse()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    flds = String.split(temp, "],[")

    matrix =
    for row <- flds do
      for col <- String.split(row, ",") do
        String.to_integer(col)
      end
    end

    "matrix = [" <> Mylib.intIntList_to_string(matrix) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.modified_matrix(matrix)
      "result = [" <> Mylib.intIntList_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
