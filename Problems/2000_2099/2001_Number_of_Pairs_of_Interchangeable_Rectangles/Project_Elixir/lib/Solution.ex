defmodule Solution do
  # 516ms - 580ms
  @spec interchangeable_rectangles(rectangles :: [[integer]]) :: integer
  def interchangeable_rectangles(rectangles) do
    interchangeable_rectangles(rectangles, %{}, 0)
  end

  @spec interchangeable_rectangles(rectangles :: [[integer]], cnts :: %{}, ans :: integer) :: integer
  def interchangeable_rectangles([head | tail], cnts, ans) do
    ratio = Enum.at(head, 0) / Enum.at(head, 1)
    cur = Map.get(cnts, ratio, 0)
    interchangeable_rectangles(tail, Map.put(cnts, ratio, cur + 1) , ans + cur)
  end

  def interchangeable_rectangles([], _, ans) do
    ans
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    flds = String.replace(temp, ", ", ",")

    rectangles =
      for fld <- String.split(flds, "],[") do
        for n <- String.split(fld, ",") do
          String.to_integer(n)
        end
      end

    "rectangles = " <> Mylib.intIntList_to_string(rectangles) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.interchangeable_rectangles(rectangles)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
