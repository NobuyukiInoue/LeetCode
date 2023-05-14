defmodule Solution do
  # 619ms - 637ms
  @spec max_sum(grid :: [[integer]]) :: integer
  def max_sum(grid) do
    len_row = Enum.count(grid)
    len_col = Enum.count(Enum.at(grid, 0))
    Enum.reduce(grid, {nil, 0, 0}, fn row, {_, i, res} ->
      if i < len_row - 2 do
        {:cont, i + 1, max(res,
        Enum.reduce(row, {nil, 0, res}, fn _, {_, j, res} ->
          if j < len_col - 2 do
            {:cont, j + 1, max(res,
                  Enum.at(Enum.at(grid, i), j) + Enum.at(Enum.at(grid, i), j + 1) + Enum.at(Enum.at(grid, i), j + 2) \
                + Enum.at(Enum.at(grid, i + 1), j + 1) \
                + Enum.at(Enum.at(grid, i + 2), j) + Enum.at(Enum.at(grid, i + 2), j + 1) + Enum.at(Enum.at(grid, i + 2), j + 2)
              )
            }
          else
            {:halt, j + 1, res}
          end
        end)) |> elem(2)
        }
      else
        {:halt, i + 1, res}
      end
    end) |> elem(2)
  end

  # 627ms - 665ms
  @spec max_sum2(grid :: [[integer]]) :: integer
  def max_sum2(grid) do
    row_sums =
      for i <- 0..Enum.count(grid) - 3 do
        col_sums =
          for j <- 0..Enum.count(Enum.at(grid, i)) - 3 do
              Enum.at(Enum.at(grid, i), j) + Enum.at(Enum.at(grid, i), j + 1) + Enum.at(Enum.at(grid, i), j + 2) \
              + Enum.at(Enum.at(grid, i + 1), j + 1) \
              + Enum.at(Enum.at(grid, i + 2), j) + Enum.at(Enum.at(grid, i + 2), j + 1) + Enum.at(Enum.at(grid, i + 2), j + 2)
          end
        Enum.max(col_sums)
      end
    Enum.max(row_sums)
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

    Mylib.matrix_to_string("grid", grid) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_sum(grid)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
