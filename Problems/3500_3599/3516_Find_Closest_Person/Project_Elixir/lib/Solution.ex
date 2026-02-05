defmodule Solution do
  # 0ms
  @spec find_closest(x :: integer, y :: integer, z :: integer) :: integer
  def find_closest(x, y, z) do
    {dif_x, dif_y} = {abs(z - x), abs(z - y)}
    cond do
      dif_x < dif_y -> 1
      dif_x > dif_y -> 2
      true -> 0
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    x = String.to_integer(Enum.at(flds, 0))
    y = String.to_integer(Enum.at(flds, 1))
    z = String.to_integer(Enum.at(flds, 2))
    "x = " <>  Integer.to_string(x) <> ", y = " <> Integer.to_string(y) <> ", z = " <> Integer.to_string(z) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_closest(x, y, z)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
