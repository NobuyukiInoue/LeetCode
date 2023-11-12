defmodule Solution do
  # 327ms - 329ms
  @spec find_champion(grid :: [[integer]]) :: integer
  def find_champion(grid) do
    n = Enum.count(grid)
    Enum.reduce_while(grid, 0, fn data, i ->
      if Enum.sum(data) == n - 1 do
        {:halt, i}
      else
        {:cont, i + 1}
      end
    end)
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

    "grid = [" <> Mylib.intIntList_to_string(grid) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_champion(grid)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
