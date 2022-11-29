defmodule Solution do
  # 348ms - 391ms
  @spec number_of_cuts(n :: integer) :: integer
  def number_of_cuts(n) do
    cond do
      n == 1 ->
        0
      rem(n, 2) == 1 ->
        n
      true ->
        div(n, 2)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    n = String.to_integer(flds)
    "n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.number_of_cuts(n)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
