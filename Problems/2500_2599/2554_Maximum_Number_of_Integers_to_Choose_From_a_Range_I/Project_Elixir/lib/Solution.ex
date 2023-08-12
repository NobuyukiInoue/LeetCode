defmodule Solution do
  # 727ms - 733ms
  @spec max_count(banned :: [integer], n :: integer, max_sum :: integer) :: integer
  def max_count(banned, n, max_sum) do
    dic =
      Enum.reduce(banned, %{}, fn ban, dic ->
        Map.put(dic, ban, true)
      end)
    Enum.reduce_while(1..n, {0, 0}, fn i, {ans, total} ->
      if total + i > max_sum do
        {:halt, {ans, total}}
      else
        if Map.get(dic, i) == nil do
          {:cont, {ans + 1, total + i}}
        else
          {:cont, {ans, total}}
        end
      end
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    banned = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    n = Enum.at(flds, 1) |> String.to_integer()
    max_sum = Enum.at(flds, 2) |> String.to_integer()
    "banned = [" <>  Mylib.intList_to_string(banned) <> "], n = " <> Integer.to_string(n) <> ", max_sum = " <> Integer.to_string(max_sum) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_count(banned, n, max_sum)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
