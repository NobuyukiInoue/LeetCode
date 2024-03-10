defmodule Solution do
  # 507ms - 584ms
  @spec find_the_prefix_common_array(a :: [integer], b :: [integer]) :: [integer]
  def find_the_prefix_common_array(a, b) do
    Enum.zip_reduce(a, b, {0, %{}, []}, fn a, b, {total, cnts, c} ->
      cnts = Map.put(cnts, a, Map.get(cnts, a, 0) + 1)
      total =
        if cnts[a] == 2 do
          total + 1
        else
          total
        end
      cnts = Map.put(cnts, b, Map.get(cnts, b, 0) + 1)
      total =
        if cnts[b] == 2 do
          total + 1
        else
          total
        end
      {total, cnts, [total] ++ c}
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

    a =
      for num <- String.split(Enum.at(flds, 0), ",") do
        String.to_integer(num)
      end
    b =
      for num <- String.split(Enum.at(flds, 1), ",") do
        String.to_integer(num)
      end

    "a = [" <> Mylib.intList_to_string(a) <> "], b = [" <> Mylib.intList_to_string(b) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_the_prefix_common_array(a, b)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
