defmodule Solution do
  # 418ms - 453ms
  @spec kth_grammar(n :: integer, k :: integer) :: integer
  def kth_grammar(n, k) do
    helper(k - 1, 0)
  end

  @spec helper(order :: integer, change :: integer) :: integer
  def helper(0, change) do
    rem(change, 2)
  end

  def helper(order, change) do
    if rem(order, 2) == 1 do
      helper(div(order, 2), change + 1)
    else
      helper(div(order, 2), change)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    n = Enum.at(flds, 0) |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()
    "n = " <> Integer.to_string(n) <> ", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.kth_grammar(n, k)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
