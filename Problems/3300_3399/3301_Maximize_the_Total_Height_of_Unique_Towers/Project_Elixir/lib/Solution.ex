defmodule Solution do
  # 168ms - 205ms
  @spec maximum_total_sum(maximum_height :: [integer]) :: integer
  def maximum_total_sum(maximum_height) do
    maximum_height = Enum.sort(maximum_height, :desc)
    Enum.reduce_while(maximum_height, {0, maximum_height |> hd}, fn num, {ans, cur} ->
      cur = min(cur, num)
      if cur <= 0 do
        {:halt, {-1, cur}}
      else
        {:cont, {ans + cur, cur - 1}}
      end
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    maximum_height = for n <- String.split(flds, ",") do String.to_integer(n) end
    "maximum_height = [" <> Mylib.intList_to_string(maximum_height) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.maximum_total_sum(maximum_height)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
