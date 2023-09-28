defmodule Solution do
  # 294ms - 388ms
  @spec check_valid_grid(grid :: [[integer]]) :: boolean
  def check_valid_grid(grid) do
    {_, dic} =
      Enum.reduce(grid, {0, %{}}, fn row, {i, dic} ->
        {_, dic} =
          Enum.reduce(row, {0, dic}, fn col, {j, dic} ->
            {j + 1, Map.put(dic, col, {i, j})}
          end)
        {i + 1, dic}
      end)
    n = Enum.count(grid)**2
    {i, j} = Map.get(dic, 0)
    if i != 0 or j != 0 do
      false
    else
      Enum.reduce_while(1..n-1, {true, i, j}, fn idx, {_, i, j} ->
        {n_i, n_j} = Map.get(dic, idx)
        if abs(n_i - i) == 1 and abs(n_j - j) == 2 or abs(n_i - i) == 2 and abs(n_j - j) == 1 do
          {:cont, {true, n_i, n_j}}
        else
          {:halt, {false, n_i, n_j}}
        end
      end) |> elem(0)
    end
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
      result = Solution.check_valid_grid(grid)
      "result = " <>  to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
