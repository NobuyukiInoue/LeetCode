defmodule Solution do
  # 0ms - 10ms
  @spec stable_mountains(height :: [integer], threshold :: integer) :: [integer]
  def stable_mountains(height, threshold) do
    Enum.reduce(height |> tl, {height |> hd, 1, []}, fn hei, {prev, i, ans} ->
      if prev > threshold do
        {hei, i + 1, [i] ++ ans}
      else
        {hei, i + 1, ans}
      end
    end)
    |> elem(2)
    |> Enum.reverse()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    height =
      for num <- String.split(Enum.at(flds, 0), ",") do
          String.to_integer(num)
      end

    threshold = String.to_integer(Enum.at(flds, 1))
    "height = [" <> Mylib.intList_to_string(height) <> "], threshold = " <> Integer.to_string(threshold) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.stable_mountains(height, threshold)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
