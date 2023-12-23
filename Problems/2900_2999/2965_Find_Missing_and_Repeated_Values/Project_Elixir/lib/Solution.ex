defmodule Solution do
  # 300ms - 370ms
  @spec find_missing_and_repeated_values(grid :: [[integer]]) :: [integer]
  def find_missing_and_repeated_values(grid) do
    cnts =
      Enum.reduce(grid, Map.new(), fn row, cnts ->
        Enum.reduce(row, cnts, fn col, cnts ->
          Map.put(cnts, col, Map.get(cnts, col, 0) + 1)
        end)
      end)
    n = Enum.count(grid)
    {a, b} =
      Enum.reduce(1..n*n, {0, 0}, fn i, {a, b} ->
        cnt = Map.get(cnts, i, 0)
        cond do
          cnt == 2 ->
            {i, b}
          cnt == 0 ->
            {a, i}
          true ->
            {a, b}
        end
      end)
    [a, b]
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

    "grid = " <> Mylib.intIntList_to_string(grid) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_missing_and_repeated_values(grid)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
