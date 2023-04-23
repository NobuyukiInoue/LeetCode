defmodule Solution do
  # 297ms - 314ms
  @spec find_column_width(grid :: [[integer]]) :: [integer]
  def find_column_width(grid) do
    find_column_width(grid, for _ <- Enum.at(grid, 0) do 0 end)
  end

  @spec find_column_width(grid :: [[integer]], ans :: [integer]) :: [integer]
  def find_column_width([head | tail], ans) do
    find_column_width(tail, column_width(ans, 0, head))
  end

  def find_column_width([], ans) do
    ans
  end

  @spec column_width(ans :: [integer], idx :: integer, row :: [integer]) :: [integer]
  def column_width(ans, idx, [head | tail]) do
    column_width(List.replace_at(ans, idx, max(Enum.at(ans, idx), String.length(Integer.to_string(head)))), idx + 1, tail)
  end

  def column_width(ans, _, []) do
    ans
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
      result = Solution.find_column_width(grid)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
