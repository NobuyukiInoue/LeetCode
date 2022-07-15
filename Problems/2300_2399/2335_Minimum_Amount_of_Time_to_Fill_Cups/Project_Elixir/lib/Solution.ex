defmodule Solution do
  # 335ms - 338ms
  @spec fill_cups(amount :: [integer]) :: integer
  def fill_cups(amount) do
    max(Enum.max(amount), div(Enum.sum(amount) + 1, 2))
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    amount = for n <- String.split(flds, ",") do String.to_integer(n) end
    "ammount = [" <> Mylib.intList_to_string(amount) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.fill_cups(amount)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
