defmodule Solution do
  # 1377ms - 1427ms
  @spec count_sub_islands(grid1 :: [[integer]], grid2 :: [[integer]]) :: integer
  def count_sub_islands(grid1, grid2) do
    m_grid1 =
      Enum.reduce(grid1, {0, %{}}, fn row, {i, m_grid} ->
        m_row =
          Enum.reduce(row, {0, %{}}, fn col, {j, m_row} ->
            {j + 1, Map.put(m_row, j, col)}
          end)
          |> elem(1)
        {i + 1, Map.put(m_grid, i, m_row)}
      end)
      |> elem(1)
    m_grid2 =
      Enum.reduce(grid2, {0, %{}}, fn row, {i, m_grid} ->
        m_row =
          Enum.reduce(row, {0, %{}}, fn col, {j, m_row} ->
            {j + 1, Map.put(m_row, j, col)}
          end)
          |> elem(1)
        {i + 1, Map.put(m_grid, i, m_row)}
      end)
      |> elem(1)

    r = Enum.count(grid1)
    c = Enum.count(grid1 |> hd)
    Enum.reduce(0..r-1, {0, m_grid2}, fn i, {ans, m_grid2} ->
      Enum.reduce(0..c-1, {ans, m_grid2}, fn j, {ans, m_grid2} ->
        if m_grid2[i][j] == 1 do
          {res, m_grid2} = dfs(m_grid1, m_grid2, i, j, r, c)
          if res do
            {ans + 1, m_grid2}
          else
            {ans, m_grid2}
          end
        else
          {ans, m_grid2}
        end
      end)
    end)
    |> elem(0)
  end

  @spec dfs(m_grid1 :: %{}, m_grid2 :: %{}, i :: integer, j :: integer, r :: integer, c :: integer) :: {res :: bool, m_grid2 :: %{}}
  def dfs(m_grid1, m_grid2, i, j, r, c) do
    if 0 <= i and i < r and 0 <= j and j < c and m_grid2[i][j] == 1 do
      if m_grid1[i][j] != 1 do
        {false, m_grid2}
      else
        m_grid2 = Map.put(m_grid2, i, Map.put(m_grid2[i], j, -1))
        dirr = [%{0 => 0, 1 => 1}, %{0 => 1, 1 => 0}, %{0 => -1, 1 => 0}, %{0 => 0, 1 => -1}]
        Enum.reduce(dirr, {true, m_grid2}, fn d, {isSubIsland, m_grid2} ->
          {res, m_grid2} = dfs(m_grid1, m_grid2, i + d[0], j + d[1], r, c)
          if isSubIsland and res do
            {true, m_grid2}
          else
            {false, m_grid2}
          end
        end)
      end
    else
      {true, m_grid2}
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[[", "")
    temp = String.replace(temp, "]]]", "")
    flds = String.split(temp, "]],[[")

    grid1 =
      for row <- String.split(Enum.at(flds, 0), "],[") do
        for col <- String.split(row, ",") do
          String.to_integer(col)
        end
      end

      grid2 =
      for row <- String.split(Enum.at(flds, 1), "],[") do
        for col <- String.split(row, ",") do
          String.to_integer(col)
        end
      end

    "grid1 = [" <> Mylib.intIntList_to_string(grid1) |> IO.puts()
    "grid2 = [" <> Mylib.intIntList_to_string(grid2) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_sub_islands(grid1, grid2)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
