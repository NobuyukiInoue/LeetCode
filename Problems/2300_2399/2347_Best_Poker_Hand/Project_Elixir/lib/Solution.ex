defmodule Solution do
  # 360ms - 410ms
  @spec best_hand(ranks :: [integer], suits :: [char]) :: String.t()
  def best_hand(_ranks, [a, a, a, a, a]), do: "Flush"

  def best_hand(ranks, _suits) do
    ranks
    |> Enum.reduce(%{}, fn r, acc ->
      Map.update(acc, r, 1, &(&1 + 1))
    end)
    |> Map.values()
    |> Enum.max()
    |> then(fn v ->
      case v do
        1 -> "High Card"
        2 -> "Pair"
        _ -> "Three of a Kind"
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, "],[")

    ranks = for n <- String.split(Enum.at(flds, 0), ",") do String.to_integer(n) end
    "ranks = [" <> Mylib.intList_to_string(ranks) <> "]" |> IO.puts()

    suits = String.split(Enum.at(flds, 1), ",")
    "suits = [" <> Enum.join(suits) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.best_hand(ranks, suits)
      "result = \"" <> result <> "\""|> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
