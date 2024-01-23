defmodule Solution do
  # 268ms - 300ms
  @spec watering_plants(plants :: [integer], capacity :: integer) :: integer
  def watering_plants(plants, capacity) do
    Enum.reduce(plants, {0, capacity, 0}, fn cur, {i, water, ans} ->
      if cur <= water do
        {i + 1, water - cur, ans + 1}
      else
        {i + 1, capacity - cur, ans + 2*i + 1}
      end
    end) |> elem(2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    plants = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    capacity = Enum.at(flds, 1) |> String.to_integer()
    "plants = [" <>  Mylib.intList_to_string(plants) <> "], capacity = " <> Integer.to_string(capacity) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.watering_plants(plants, capacity)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
