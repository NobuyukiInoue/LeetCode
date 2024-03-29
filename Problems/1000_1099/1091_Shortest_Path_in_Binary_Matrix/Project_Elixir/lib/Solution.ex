defmodule Solution do
  # 786ms - 805ms
  @spec shortest_path_binary_matrix(grid :: [[integer]]) :: integer
  def shortest_path_binary_matrix(grid) do
    {_, m_grid} =
      Enum.reduce(grid, {0, MapSet.new()}, fn row, {i, m_grid} ->
        {_j, m_grid_row} =
          Enum.reduce(row, {0, MapSet.new()}, fn col, {j, m_grid_row} ->
            if col == 0 do
              {j + 1, MapSet.put(m_grid_row, {i, j})}
            else
              {j + 1, m_grid_row}
            end
          end)
        {i + 1, MapSet.union(m_grid, m_grid_row)}
      end)
    m = Enum.count(grid)
    visited = MapSet.new()
    if (not MapSet.member?(m_grid, {0, 0})) or (not MapSet.member?(m_grid, {m - 1, m - 1})) do
      -1
    else
      que = :gb_sets.new()
      dfs(m_grid, m, :gb_sets.add_element({1, 0, 0}, que), MapSet.put(visited, {0, 0}))
    end
  end

  @empty_q :gb_sets.empty()
  @spec dfs(m_grid :: map(), m :: non_neg_integer, que :: any, visited :: map()) :: integer
  def dfs(_m_grid, _m, @empty_q, _visited) do
    -1
  end

  def dfs(m_grid, m, que, visited) do
    {{dist, i, j}, que} = :gb_sets.take_smallest(que)
    if {i, j} == {m - 1, m - 1} do
      dist
    else
      {que, visited} =
        Enum.reduce([{1, 1}, {1, -1}, {-1, -1}, {1, 0}, {0, 1}, {0, -1}, {-1, 1}, {-1, 0}, {-1, 1}], {que, visited}, fn {di, dj}, {que, visited} ->
          {ni, nj} = {i + di, j + dj}
          cond do
            MapSet.member?(visited, {ni, nj}) ->
              {que, visited}
            ni < 0 or m <= ni or nj < 0 or m <= nj ->
              {que, visited}
            MapSet.member?(m_grid, {ni, nj}) ->
              {:gb_sets.add_element({dist + 1, ni, nj}, que), MapSet.put(visited, {ni, nj})}
            true ->
              {que, visited}
          end
        end)
      dfs(m_grid, m, que, visited)
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
