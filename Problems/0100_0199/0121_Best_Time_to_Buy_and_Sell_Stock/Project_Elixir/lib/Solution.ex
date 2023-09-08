defmodule Solution do
  # 332ms - 367ms
  @spec max_profit(prices :: [integer]) :: integer
  def max_profit(prices) do
    Enum.reduce(prices, {0, 100_000}, fn price, {v_max, v_min} ->
      v_min = if v_min > price, do: price, else: v_min
      v_max = if price - v_min > v_max, do: price - v_min, else: v_max
      {v_max, v_min}
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    prices = for n <- String.split(flds, ",") do String.to_integer(n) end
    "prices = [" <> Mylib.intList_to_string(prices) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_profit(prices)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
