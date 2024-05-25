defmodule Solution do
  # 394ms - 424ms
  @spec satisfies_conditions(grid :: [[integer]]) :: boolean
  def satisfies_conditions(grid) do
    {m, n} = {Enum.count(grid), Enum.count(grid |> hd)}
    m_grid =
      Enum.reduce(grid, {0, %{}}, fn row, {i, m_grid} ->
        {_j, m_grid} =
          Enum.reduce(row, {0, m_grid}, fn col, {j, m_grid} ->
            {j + 1, Map.put(m_grid, {i, j}, col)}
          end)
        {i + 1, m_grid}
      end)
      |> elem(1)
    Enum.reduce_while(0..m-1, true, fn i, _res ->
      res =
        Enum.reduce_while(0..n-1, true, fn j, _res ->
          cond do
            j < n-1 and m_grid[{i, j}] == m_grid[{i, j + 1}] ->
              {:halt, false}
            i < m-1 and m_grid[{i, j}] != m_grid[{i + 1,j}] ->
              {:halt, false}
            true ->
              {:cont, true}
          end
        end)
      if res do
        {:cont, res}
      else
        {:halt, res}
      end
    end)
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
      result = Solution.satisfies_conditions(grid)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
