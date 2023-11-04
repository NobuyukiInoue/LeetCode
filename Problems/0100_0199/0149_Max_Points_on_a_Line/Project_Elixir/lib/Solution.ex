defmodule Solution do
  # 296ms - 314ms
  @spec max_points(points :: [[integer]]) :: integer
  def max_points(points) do
    m = Enum.count(points)
    if m <= 2 do
      m
    else
      Enum.reduce_while(0..m-1, 0, fn i, res ->
        if i + 1 == m - 1 do
          {:halt, res}
        else
          {cur, overlap, _} =
            Enum.reduce((i+1)..(m-1), {0, 0, Map.new()}, fn j, {cur, overlap, lines} ->
              dx = Enum.at(Enum.at(points, i), 0) - Enum.at(Enum.at(points, j), 0)
              dy = Enum.at(Enum.at(points, i), 1) - Enum.at(Enum.at(points, j), 1)
              if dx == 0 and dy == 0 do
                {cur, overlap + 1, lines}
              else
                key =
                  if dx == 0 do
                    # Float.max_finite
                    1.7976931348623157e308
                  else
                    10.0*dy/dx
                  end
                lines = Map.put(lines, key, Map.get(lines, key, 1) + 1)
                {max(cur, Map.get(lines, key)), overlap, lines}
              end
            end)
          {:cont, max(res, cur + overlap)}
        end
      end)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    points =
    for fld <- flds do
      for n <- String.split(fld, ",") do
        String.to_integer(n)
      end
    end

    "points = [" <> Mylib.intIntList_to_string(points) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_points(points)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
