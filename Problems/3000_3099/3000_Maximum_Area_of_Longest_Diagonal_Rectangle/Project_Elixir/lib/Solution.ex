defmodule Solution do
  # 338ms - 350ms
  @spec area_of_max_diagonal(dimensions :: [[integer]]) :: integer
  def area_of_max_diagonal(dimensions) do
    Enum.reduce(dimensions, {0, 0}, fn rect, {max_diag, max_area}->
      l = rect |> hd
      w = rect |> tl |> hd
      area = l*w
      diag = l*l + w*w
      if diag > max_diag or diag == max_diag and area > max_area do
        {diag, area}
      else
        {max_diag, max_area}
      end
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    dimensions =
    for fld <- flds do
      for n <- String.split(fld, ",") do
        String.to_integer(n)
      end
    end

    "dimensions = " <> Mylib.intIntList_to_string(dimensions) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.area_of_max_diagonal(dimensions)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
