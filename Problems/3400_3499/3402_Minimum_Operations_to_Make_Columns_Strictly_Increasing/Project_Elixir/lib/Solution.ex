defmodule Solution do
  # 16ms - 18ms
  @spec minimum_operations(grid :: [[integer]]) :: integer
  def minimum_operations(grid) do
    Enum.reduce(grid, {0, %{}}, fn row, {ans, m_cur} ->
      {_col_idx, ans, m_cur} =
        Enum.reduce(row, {0, ans, m_cur}, fn col, {col_idx, ans, m_cur} ->
#         "col_idx = " <> Integer.to_string(col_idx) <> ", ans = " <> Integer.to_string(ans) |> IO.puts()
          m_cur = Map.put(m_cur, col_idx, Map.get(m_cur, col_idx, -1))
#         print_map(m_cur)
          if col <= m_cur[col_idx] do
            {col_idx + 1, ans + m_cur[col_idx] - col + 1, Map.put(m_cur, col_idx, m_cur[col_idx] + 1)}
          else
            {col_idx + 1, ans, Map.put(m_cur, col_idx, col)}
          end
        end)
      {ans, m_cur}
    end) |> elem(0)
  end

  @spec print_map(m_cur :: %{}) :: None
  def print_map(m_cur) do
    res =
    for key <- Map.keys(m_cur) do
      m_cur[key]
    end
    "m_keys = {" <> Enum.join(res, ", ") <> "}" |> IO.puts()
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
      result = Solution.minimum_operations(grid)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
