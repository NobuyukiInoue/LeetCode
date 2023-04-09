defmodule Solution do
  # 592ms - 654ms
  @spec dist_money(money :: integer, children :: integer) :: integer
  def dist_money(money, children) do
    new_money = money -  children
    cond do
      new_money < 0 ->
        -1
      div(new_money, 7) == children and rem(new_money, 7) == 0 ->
        children
      div(new_money, 7) == children - 1 and rem(new_money, 7) == 3 ->
        children - 2
      true ->
        min(children - 1, div(new_money, 7))
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    money = Enum.at(flds, 0) |> String.to_integer()
    children = Enum.at(flds, 1) |> String.to_integer()
    "money = " <> Integer.to_string(money) <> ", children = " <> Integer.to_string(children) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.dist_money(money, children)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
