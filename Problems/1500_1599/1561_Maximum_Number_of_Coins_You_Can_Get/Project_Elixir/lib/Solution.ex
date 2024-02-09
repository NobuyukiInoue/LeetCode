defmodule Solution do
  # 555ms - 597ms
  @spec max_coins(piles :: [integer]) :: integer
  def max_coins(piles) do
    n = Enum.count(piles)
    limit = div(n*2, 3)
    Enum.reduce_while(Enum.sort(piles, :desc), {0, 0}, fn pile, {i, ans} ->
      cond do
        i >= limit -> {:halt, {i + 1, ans}}
        rem(i, 2) == 1 -> {:cont, {i + 1, ans + pile}}
        true -> {:cont, {i + 1, ans}}
      end
    end) |> elem(1)
  end

  # 515ms - 621ms
  @spec max_coins2(piles :: [integer]) :: integer
  def max_coins2(piles) do
    piles
    |> Enum.sort()
    |> Enum.drop(div(length(piles), 3))
    |> Stream.take_every(2)
    |> Enum.sum()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    piles = for n <- String.split(flds, ",") do String.to_integer(n) end
    "piles = [" <> Mylib.intList_to_string(piles) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_coins(piles)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
