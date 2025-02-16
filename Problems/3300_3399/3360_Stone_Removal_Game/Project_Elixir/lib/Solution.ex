defmodule Solution do
  # 0ms
  @spec can_alice_win(n :: integer) :: boolean
  def can_alice_win(n) do
    rem(count_game(n, 10, 0), 2) != 0
  end

  @spec count_game(n :: integer, pile :: integer, count :: integer) :: integer
  def count_game(n, pile, count) when n < pile do
    count
  end

  def count_game(n, pile, count) do
    count_game(n - pile, pile - 1, count + 1)
  end

  @spec loop_main(temp :: String.t) :: :ox
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")

    n = String.to_integer(flds)
    "n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.can_alice_win(n)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
