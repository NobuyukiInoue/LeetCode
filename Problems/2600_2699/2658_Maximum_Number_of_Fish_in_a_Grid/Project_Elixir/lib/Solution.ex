defmodule Solution do
  # 708ms - 733ms
  @spec find_max_fish(grid :: [[integer]]) :: integer
  def find_max_fish(grid) do
    {_, m_grid} =
      Enum.reduce(grid, {0, %{}}, fn row, {i, m_grid} ->
        {_, m_grid} =
          Enum.reduce(row, {0, m_grid}, fn col, {j, m_grid} ->
            if col != 0 do
              {j + 1, Map.put(m_grid, {i, j}, col)}
            else
              {j + 1, m_grid}
            end
          end)
        {i + 1, m_grid}
      end)
    {m, n} = {Enum.count(grid), Enum.count(grid |> hd)}
    Enum.reduce(Map.keys(m_grid), {m_grid, 0}, fn {i, j}, {m_grid, ans} ->
      if Map.has_key?(m_grid, {i, j}) do
        {m_grid, cnt} = dfs(m_grid, m, n, i, j, m_grid[{i, j}])
#       {m_grid, cnt} = dfs(m_grid, i, j, m_grid[{i, j}])   # 723ms - 815ms
        {m_grid, max(ans, cnt)}
      else
        {m_grid, ans}
      end
    end)
    |> elem(1)
  end

  @spec dfs(m_grid :: %{}, m :: integer, n :: integer, i :: integer, j :: integer, cnt :: integer) :: {%{}, integer}
  def dfs(m_grid, m, n, i, j, cnt) do
    m_grid = Map.delete(m_grid, {i, j})
    Enum.reduce([{1, 0}, {-1, 0}, {0, 1}, {0, -1}], {m_grid, cnt}, fn {di, dj}, {m_grid, cnt} ->
      {ni, nj} = {i + di, j + dj}
      cond do
        ni < 0 or m <= ni or nj < 0 or n <= nj ->
          {m_grid, cnt}
        Map.has_key?(m_grid, {ni, nj}) ->
          {m_grid, n_cnt} = dfs(m_grid, m, n, ni, nj, m_grid[{ni, nj}])
          {m_grid, cnt + n_cnt}
        true ->
          {m_grid, cnt}
      end
    end)
  end

  # 723ms - 815ms
  @spec dfs2(m_grid :: %{}, i :: integer, j :: integer, cnt :: integer) :: {%{}, integer}
  def dfs2(m_grid, i, j, cnt) do
    m_grid = Map.delete(m_grid, {i, j})
    Enum.reduce([{1, 0}, {-1, 0}, {0, 1}, {0, -1}], {m_grid, cnt}, fn {di, dj}, {m_grid, cnt} ->
      {ni, nj} = {i + di, j + dj}
      cond do
        Map.has_key?(m_grid, {ni, nj}) ->
          {m_grid, n_cnt} = dfs2(m_grid, ni, nj, m_grid[{ni, nj}])
          {m_grid, cnt + n_cnt}
        true ->
          {m_grid, cnt}
      end
    end)
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
      result = Solution.find_max_fish(grid)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
