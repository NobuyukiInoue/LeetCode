defmodule Solution do
  # 449ms - 582ms
  @spec count_squares(matrix :: [[integer]]) :: integer
  def count_squares(matrix) do
    m_matrix =
      Enum.reduce(matrix, {0, %{}}, fn row, {i, rows} ->
        cols =
          Enum.reduce(row, {0, %{}}, fn col, {j, cols} ->
            {j + 1, Map.put(cols, j, col)}
          end)
          |> elem(1)
        {i + 1, Map.put(rows, i, cols)}
      end)
      |> elem(1)

    {m, n} = {Enum.count(matrix), Enum.count(matrix |> hd)}
    Enum.reduce(0..m-1, {m_matrix, 0}, fn i, {m_matrix, count} ->
      m_matrix =
        Enum.reduce(0..n-1, m_matrix, fn j, m_matrix ->
          if m_matrix[i][j] == 1 and (i != 0 and j != 0) do
            Map.put(m_matrix, i, Map.put(m_matrix[i], j, Enum.min([m_matrix[i-1][j-1], m_matrix[i-1][j], m_matrix[i][j-1]]) + 1))
          else
            m_matrix
          end
        end)
      {m_matrix, count + (m_matrix[i] |> Map.values |> Enum.sum())}
    end)
    |> elem(1)
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
      result = Solution.count_squares(matrix)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
