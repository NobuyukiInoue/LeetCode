defmodule Solution do
  # 339ms - 347ms
  @spec max_height_of_triangle(red :: integer, blue :: integer) :: integer
  def max_height_of_triangle(red, blue) when red < blue do
      max_height_of_triangle(blue, red)
  end

  def max_height_of_triangle(red, blue) do
    h1 = trunc(:math.sqrt(blue*4 + 1))
    h2 = trunc(:math.sqrt(blue))*2
    cond do
      div((h1+1)**2, 4) <= red ->
        h1
      div((h2+1)**2-1, 4) <= red ->
        h2
      div((h1-1)**2, 4) <= red ->
        h1 - 1
      true ->
        h2 - 1
    end
  end

  @spec loop_main(temp :: String.t) :: :oblue
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    red = String.to_integer(Enum.at(flds, 0))
    blue = String.to_integer(Enum.at(flds, 1))
    "red = " <> Integer.to_string(red) <> ", blue = " <> Integer.to_string(blue) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_height_of_triangle(red, blue)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
