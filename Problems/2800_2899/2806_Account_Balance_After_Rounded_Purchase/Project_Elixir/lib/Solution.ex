defmodule Solution do
  # 215ms - 269ms
  @spec account_balance_after_purchase(purchase_amount :: integer) :: integer
  def account_balance_after_purchase(purchase_amount) do
    100 - div(purchase_amount + 5, 10)*10
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")
    purchase_amount = String.to_integer(flds)
    "purchase_amount = " <> to_string(purchase_amount) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.account_balance_after_purchase(purchase_amount)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
