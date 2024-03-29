defmodule Solution do
  # 336ms - 354ms
  @spec largest_vals_from_labels(values :: [integer], labels :: [integer], num_wanted :: integer, use_limit :: integer) :: integer
  def largest_vals_from_labels(values, labels, num_wanted, use_limit) do
    [values, labels]
    |> Enum.zip()
    |> Enum.sort()
    |> Enum.reverse()
    |> Enum.reduce_while({0, num_wanted, %{}}, fn {value, label}, {ans, num_wanted, used_count} ->
      cond do
        num_wanted == 0 ->
          {:halt, {ans, num_wanted, used_count}}
        Map.get(used_count, label, 0) >= use_limit ->
          {:cont, {ans, num_wanted, used_count}}
        true ->
          {:cont, {ans + value, num_wanted - 1, Map.put(used_count, label, Map.get(used_count, label, 0) + 1)}}
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

    values =
      for num <- String.split(Enum.at(flds, 0), ",") do
          String.to_integer(num)
      end
    labels =
      for num <- String.split(Enum.at(flds, 1), ",") do
          String.to_integer(num)
      end
    num_wanted = String.to_integer(Enum.at(flds, 2))
    use_limit = String.to_integer(Enum.at(flds, 3))

    "values = [" <> Mylib.intList_to_string(values) <> "], labels = [" <> Mylib.intList_to_string(labels) <> "], num_wanted = " <> Integer.to_string(num_wanted) <> ", use_limit = " <> Integer.to_string(use_limit) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.largest_vals_from_labels(values, labels, num_wanted, use_limit)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
