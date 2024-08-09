defmodule Solution do
  # 283ms - 361ms
  @spec number_of_alternating_groups(colors :: [integer]) :: integer
  def number_of_alternating_groups(colors) do
    n = Enum.count(colors)
    Enum.reduce(0..n-1, 0, fn i, ans ->
      j =
        if i + 1 < n do
          i + 1
        else
          i + 1 - n
        end
      if Enum.at(colors, i) == Enum.at(colors, j) do
        ans
      else
        k =
          if i + 2 < n do
              i + 2
          else
              i + 2 - n
          end
        if Enum.at(colors, j) ==  Enum.at(colors, k) do
          ans
        else
          ans + 1
        end
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    colors = for n <- String.split(flds, ",") do String.to_integer(n) end
    "colors = [" <> Mylib.intList_to_string(colors) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.number_of_alternating_groups(colors)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
