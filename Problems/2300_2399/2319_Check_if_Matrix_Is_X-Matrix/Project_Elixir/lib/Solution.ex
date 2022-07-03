defmodule Solution do
  @spec check_x_matrix(grid :: [[integer]]) :: boolean
  # 417ms - 477ms
  def check_x_matrix(grid) do
    len = Enum.count(grid)
    grid
    |> Enum.with_index()
    |> Enum.reduce_while(true, fn {row, i}, acc ->
      row
      |> Enum.with_index()
      |> Enum.reduce_while(acc, fn {n, j}, _ ->
        cond do
          (i == j || i + j + 1 == len) && n == 0 -> {:halt, false}
          i != j && i + j + 1 != len && n != 0 -> {:halt, false}
          true -> {:cont, true}
        end
      end)
      # Elixir ver1.52 later.
#      |> then(fn r ->
#        if r do
#          {:cont, true}
#        else
#          {:halt, false}
#        end
#      end)
      |> (fn r ->
        if r do
          {:cont, true}
        else
          {:halt, false}
        end
      end).()
    end)
  end

  def check_x_matrix_bad(grid) do
    len_grid = Enum.count(grid) - 1
    res =
    for i <- 0..Enum.count(grid) - 1 do
      for j <- 0..Enum.count(Enum.at(grid, i)) do
        if i == j || i + j == len_grid - 1 do
          if Enum.at(Enum.at(grid, i), j ) == 0 do
            {:halt, false}
          end
        else
          if Enum.at(Enum.at(grid, i), j ) != 0 do
            {:halt, false}
          end
        end
      end
    end
    {:cont, true}

    res |> (fn r ->
      if r do
        {:cont, true}
      else
        {:halt, false}
      end
    end).()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    grid =
    for fld <- flds do
      for n <- String.split(fld, ",") do
        String.to_integer(n)
      end
    end

    Mylibs.matrixToString("grid", grid) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.check_x_matrix(grid)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
