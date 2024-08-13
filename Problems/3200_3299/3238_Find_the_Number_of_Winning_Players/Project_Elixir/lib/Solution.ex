defmodule Solution do
  # 386ms - 403ms
  @spec winning_player_count(n :: integer, pick :: [[integer]]) :: integer
  def winning_player_count(_n, pick) do
    balls =
      Enum.reduce(pick, %{}, fn [player | [color | _]], balls ->
        Map.put(balls, {player, color}, Map.get(balls, {player, color}, 0) + 1)
      end)
    cnts =
      Enum.reduce(Map.keys(balls), %{}, fn {player, color}, cnts ->
        if balls[{player, color}] > player do
          Map.put(cnts, player, 1)
        else
          cnts
        end
      end)
    Kernel.map_size(cnts)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "]]]", "")
    flds = String.split(temp, "],[[")

    n = String.replace(Enum.at(flds, 0), "[[", "") |> String.to_integer()
    pick =
    for row <- String.split(Enum.at(flds, 1), "],[") do
      for col <- String.split(row, ",") do
        String.to_integer(col)
      end
    end

    "n = " <> Integer.to_string(n) <> ", pick = [" <> Mylib.intIntList_to_string(pick) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.winning_player_count(n, pick)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
