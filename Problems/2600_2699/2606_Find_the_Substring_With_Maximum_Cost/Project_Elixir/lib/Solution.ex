defmodule Solution do
  # 428ms - 462ms
  @spec maximum_cost_substring(s :: String.t, chars :: String.t, vals :: [integer]) :: integer
  def maximum_cost_substring(s, chars, vals) do
    char_dict = Enum.reduce(String.to_charlist(chars), {0, %{}}, fn ch, {i, dic} ->
      {i + 1, Map.put(dic, ch, Enum.at(vals, i))}
    end) |> elem(1)

    String.to_charlist(s) |>
    Enum.reduce({0, 0}, fn ch, {max_cost, curr_cost} ->
      curr_cost = curr_cost + Map.get(char_dict, ch, ch - ?a + 1)
      curr_cost =
        if curr_cost < 0 do
          0
        else
          curr_cost
        end
      {max(curr_cost, max_cost), curr_cost}
      end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, "],[")

    s = Enum.at(flds, 0)
    chars = Enum.at(flds, 1)
    vals = for num <- String.split(Enum.at(flds, 2), ",") do String.to_integer(num) end
    "s = \"" <> s <> "\", chars = \"" <> chars <> "\", vals = " <> Mylib.stringArray_to_string(vals) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.maximum_cost_substring(s, chars, vals)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
