defmodule Solution do
  # 420ms - 440ms
  @spec count_complete_day_pairs(hours :: [integer]) :: integer
  def count_complete_day_pairs(hours) do
    n = Enum.count(hours)
    if n > 1 do
      Enum.reduce(0..n-2, 0, fn i, cnt ->
        Enum.reduce(i+1..n-1, cnt, fn j, cnt ->
          if rem(Enum.at(hours, i) + Enum.at(hours, j), 24) == 0 do
            cnt + 1
          else
            cnt
          end
        end)
      end)
    else
      0
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    hour = for n <- String.split(flds, ",") do String.to_integer(n) end
    "hour = [" <> Mylib.intList_to_string(hour) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_complete_day_pairs(hour)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
