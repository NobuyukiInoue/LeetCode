defmodule Solution do
  # 351ms - 398ms
  @spec number_of_child(n :: integer, k :: integer) :: integer
  def number_of_child(n, k) do
    n = n - 1
    {rounds, remainder} = {div(k, n), rem(k, n)}
    if rem(rounds, 2) == 0 do
      remainder
    else
      n - remainder
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    n = String.to_integer(Enum.at(flds, 0))
    k = String.to_integer(Enum.at(flds, 1))
    "n = " <> Integer.to_string(n) <> ", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.number_of_child(n, k)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
