defmodule Solution do
  # Time Limit Exceeded. (71/76)
  @spec contains_cycle(grid :: [[char]]) :: boolean
  def contains_cycle(grid) do
    {_, m_grid, visited} =
      Enum.reduce(grid, {0, %{}, %{}}, fn row, {i, m_grid, visited} ->
        {_, m_grid, visited} =
          Enum.reduce(row, {0, m_grid, visited}, fn col, {j, m_grid, visited} ->
            {j + 1, Map.put(m_grid, {i, j}, col), Map.put(visited, {i, j}, false)}
          end)
        {i + 1, m_grid, visited}
        end)

    {m, n} = {Enum.count(grid), Enum.count(grid |> hd)}
    Enum.reduce_while(0..m-1, {false, visited}, fn i, {_res, _visited} ->
      {res, visited} =
        Enum.reduce_while(0..n-1, {false, visited}, fn j, {_res, visited} ->
          if not visited[{i, j}] do
            {res, visited} = bfs(m_grid, m, n, i, j, -1, -1, visited)
            if res do
              {:halt, {true, visited}}
            else
              {:cont, {false, visited}}
            end
          else
            {:cont, {false, visited}}
          end
        end)
      if res do
        {:halt, {true, visited}}
      else
        {:cont, {false, visited}}
      end
    end)
    |> elem(0)
  end

  @spec bfs(m_grid :: %{}, m :: integer, n :: integer, i :: Integer, j :: Integer, x :: Integer, y :: Integer, visited :: %{}) :: {Boolean, %{}}
  def bfs(m_grid, m, n, i, j, x, y, visited) do
    visited = Map.put(visited, {i, j}, true)
    que = :gb_sets.new()
    bfs_while(m_grid, m, n, i, j, x, y, :gb_sets.add_element({0, i, j, x, y}, que), visited, false)
  end

  @empty_q :gb_sets.empty()
  @spec bfs_while(m_grid :: %{}, m :: integer, n :: integer, i :: integer, j :: integer, x :: integer, y :: integer, que :: any, visited :: %{}, res :: boolean()) :: {Boolean, %{}}
  def bfs_while(_m_grid, _m, _n, _i, _j, _x, _y, @empty_q, visited, res) do
    {res, visited}
  end

  def bfs_while(m_grid, m, n, i, j, x, y, que, visited, _res) do
    ch = m_grid[{i, j}]
    l = :gb_sets.size(que)
    {res, que, visited} =
      Enum.reduce_while(0..l-1, {false, que, visited}, fn _k, {_res, que, visited} ->
        {{cnt, cur_i, cur_j, cur_x, cur_y}, que} = :gb_sets.take_smallest(que)
        {res, _cnt, que, visited} =
          Enum.reduce_while([{0, 1}, {1, 0}, {0, -1}, {-1, 0}], {false, cnt, que, visited}, fn {di, dj}, {_res, cnt, que, visited} ->
            {ni, nj} = {cur_i + di, cur_j + dj}
            cond do
              ni < 0 or ni >= m or nj < 0 or nj >= n or m_grid[{ni, nj}] != ch ->
                {:cont, {false, cnt, que, visited}}
              ni == cur_x and nj == cur_y ->
                {:cont, {false, cnt, que, visited}}
              visited[{ni, nj}] ->
                {:halt, {true, cnt, que, visited}}
              true ->
                {:cont, {false, cnt + 1, :gb_sets.add_element({cnt + 1, ni, nj, cur_i, cur_j}, que), Map.put(visited, {ni, nj}, true)}}
            end
        end)
        if res do
          {:halt, {true, que, visited}}
        else
          {:cont, {false, que, visited}}
        end
      end)
    if res do
      {true, visited}
    else
      bfs_while(m_grid, m, n, i, j, x, y, que, visited, false)
    end
  end

  @spec charCharGrid_to_string(arrs :: [[char]]) :: String.t
  def charCharGrid_to_string(arrs) do
    res =
      for arr <- arrs do
        "[" <> to_string(arr) <> "]"
      end
    "  " <> Enum.join(res, "\n, ")
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    flds = String.split(temp, "],[")

    grid =
    for row <- flds do
      row |> String.replace(",", "") |>  String.to_charlist()
    end

    "grid = [\n" <> charCharGrid_to_string(grid) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.contains_cycle(grid)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
