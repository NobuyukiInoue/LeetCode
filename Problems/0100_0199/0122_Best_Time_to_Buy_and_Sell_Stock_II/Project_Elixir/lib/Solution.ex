defmodule Solution do
  # 219ms - 244ms
  @spec max_profit(prices :: [integer]) :: integer
  def max_profit(prices) do
    Enum.reduce(prices, {0, prices |> hd}, fn price, {profit, prev} ->
      if price > prev do
        {profit + price - prev, price}
      else
        {profit, price}
      end
    end) |> elem(0)
  end

  # 229ms - 253ms
  @spec max_profit2(prices :: [integer]) :: integer
  def max_profit2(prices) do
    Enum.chunk_every(prices, 2, 1, :discard)
    |> Enum.map(fn [a, b] -> max(0, b - a) end)
    |> Enum.sum()
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
