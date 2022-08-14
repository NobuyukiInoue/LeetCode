defmodule Solution do
  # 359ms - 418ms
  @spec merge_similar_items(items1 :: [[integer]], items2 :: [[integer]]) :: [[integer]]
  def merge_similar_items(items1, items2) do
    map =
      items1
      |> Enum.reduce(%{}, fn [v, w], acc ->
        Map.put(acc, v, w)
      end)

    items2
    |> Enum.reduce(map, fn [v, w], acc ->
      Map.update(acc, v, w, &(&1 + w))
    end)
    |> Enum.map(fn {v, w} -> [v, w] end)
    |> Enum.sort()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[[", "")
    temp = String.replace(temp, "]]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "]],[[")

    items1 =
    for fld <- String.split(Enum.at(flds, 0), "],[") do
      for n <- String.split(fld, ",") do
        String.to_integer(n)
      end
    end
    Mylib.matrix_to_string("items1", items1) |> IO.puts()

    items2 =
      for fld <- String.split(Enum.at(flds, 1), "],[") do
        for n <- String.split(fld, ",") do
          String.to_integer(n)
        end
      end
      Mylib.matrix_to_string("items2", items2) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.merge_similar_items(items1, items2)
      "result = [" <> Mylib.intIntList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
