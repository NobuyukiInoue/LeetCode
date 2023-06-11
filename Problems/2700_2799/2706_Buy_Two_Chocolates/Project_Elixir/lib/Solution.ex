defmodule Solution do
  # 449ms - 451ms
  @spec buy_choco(prices :: [integer], money :: integer) :: integer
  def buy_choco(prices, money) do
    prices = Enum.sort(prices)
    if Enum.at(prices, 0) + Enum.at(prices, 1) <= money do
      money - (Enum.at(prices, 0) + Enum.at(prices, 1))
    else
      money
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    prices = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    money = Enum.at(flds, 1) |> String.to_integer()
    "prices = [" <>  Mylib.intList_to_string(prices) <> "], money = " <> Integer.to_string(money) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.buy_choco(prices, money)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
