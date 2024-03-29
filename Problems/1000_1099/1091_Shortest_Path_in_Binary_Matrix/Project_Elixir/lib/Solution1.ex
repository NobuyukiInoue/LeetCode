defmodule Solution1 do
  # Time Limite Exceeded. 64/90
  @spec shortest_path_binary_matrix(grid :: [[integer]]) :: integer
  def shortest_path_binary_matrix(grid) do
    {_, m_grid, visited} =
    Enum.reduce(grid, {0, %{}, %{}}, fn row, {i, m_grid, visited} ->
      {_, m_grid_row, visited_row} =
        Enum.reduce(row, {0, %{}, %{}}, fn col, {j, m_grid_row, visited_row} ->
          {j + 1, Map.put(m_grid_row, j, col), Map.put(visited_row, j, false)}
        end)
      {i + 1, Map.put(m_grid, i, m_grid_row), Map.put(visited, i, visited_row)}
      end)
    {m, n} = {map_size(m_grid), map_size(m_grid[0])}
    if m_grid[0][0] != 0 or m_grid[m - 1][n - 1] != 0 do
      -1
    else
      dfs(m_grid, m, n, [{0, 0, 1}], Map.put(visited, 0, Map.put(visited[0], 0, true)))
    end
  end

  @spec dfs(m_grid :: map(), m :: non_neg_integer, n :: non_neg_integer, que :: [{i :: integer, j :: integer, dist :: integer}], visited :: map()) :: integer
  def dfs(_m_grid, _m, _n, que, _visited) when que == [] do
    -1
  end

  def dfs(m_grid, m, n, que, visited) do
  # r_que = que |> Enum.reverse()
  # {{i, j, dist}, que} = {r_que |> hd, r_que |> tl |> Enum.reverse()}
    {{i, j, dist}, que} = {List.last(que), que |> Enum.reverse() |> tl |> Enum.reverse()}
    if i == m - 1 and j == n - 1 do
      dist
    else
      {que, visited} =
        Enum.reduce([{1, 1}, {1, -1}, {-1, 1}, {-1, -1}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}], {que, visited}, fn d, {que, visited} ->
          {di, dj} = d
          {ni, nj} = {i + di, j + dj}
          if 0 <= ni and ni < m and 0 <= nj and nj < n and (not visited[ni][nj]) and m_grid[ni][nj] == 0 do
            {[{ni, nj, dist + 1}] ++ que, Map.put(visited, i, Map.put(visited[i], j, true))}
          else
            {que, visited}
          end
        end)
      dfs(m_grid, m, n, que, visited)
    end
  end

  @spec grid_to_string(arrs :: [[integer]]) :: String.t
  def grid_to_string(arrs) do
    res =
      for arr <- arrs do
        "[" <> Mylib.intList_to_string(arr) <> "]"
      end
    "  " <> Enum.join(res, "\n, ")
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

    "grid = [\n" <> grid_to_string(grid) <> "\n]"|> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.shortest_path_binary_matrix(grid)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
