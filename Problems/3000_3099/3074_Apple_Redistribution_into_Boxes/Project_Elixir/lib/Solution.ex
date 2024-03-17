defmodule Solution do
  # 319ms - 348ms
  @spec minimum_boxes(apple :: [integer], capacity :: [integer]) :: integer
  def minimum_boxes(apple, capacity) do
    total = Enum.sum(apple)
    capacity
    |> Enum.sort()
    |> Enum.reverse
    |> Enum.reduce_while({0, 0}, fn cap, {i, t_cap} ->
      if t_cap >= total do
        {:halt, {i, t_cap}}
      else
        {:cont, {i + 1, t_cap + cap}}
      end
    end)
    |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    apple =
      for num <- String.split(Enum.at(flds, 0), ",") do
          String.to_integer(num)
      end
    capacity =
      for num <- String.split(Enum.at(flds, 1), ",") do
          String.to_integer(num)
      end

    "apple = " <> Mylib.intList_to_string(apple) <> ", capacity = " <> Mylib.intList_to_string(capacity) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_boxes(apple, capacity)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
