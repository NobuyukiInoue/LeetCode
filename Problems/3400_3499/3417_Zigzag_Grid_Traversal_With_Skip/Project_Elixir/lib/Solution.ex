defmodule Solution do
  # 18ms - 30ms
  @spec zigzag_traversal(grid :: [[integer]]) :: [integer]
  def zigzag_traversal(grid) do
    {_, res} =
      Enum.reduce(grid, {0, []}, fn row, {i, res} ->
        if rem(i, 2) == 0 do
          {i + 1, res ++ row}
        else
          {i + 1, res ++ (row |> Enum.reverse())}
        end
      end)
    Enum.reduce(res, {0, []}, fn num, {i, ans} ->
      if rem(i, 2) == 0 do
        {i + 1, ans ++ [num]}
      else
        {i + 1, ans}
      end
    end) |> elem(1)
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
      result = Solution.zigzag_traversal(grid)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
