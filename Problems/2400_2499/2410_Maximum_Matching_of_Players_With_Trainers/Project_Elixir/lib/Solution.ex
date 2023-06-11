defmodule Solution do
  # 396ms - 433ms
  @spec match_players_and_trainers(players :: [integer], trainers :: [integer]) :: integer
  def match_players_and_trainers(players, trainers) do
    match_players_and_trainers(Enum.sort(players), Enum.sort(trainers), 0)
  end

  @spec match_players_and_trainers(players :: [integer], trainers :: [integer], res :: integer) :: integer
  def match_players_and_trainers([p_hd | p_tl], [t_hd | t_tl], res) do
    if p_hd <= t_hd do
      match_players_and_trainers(p_tl, t_tl, res + 1)
    else
      match_players_and_trainers([p_hd | p_tl], t_tl, res)
    end
  end

  def match_players_and_trainers([], _, res) do
    res
  end

  def match_players_and_trainers(_, [], res) do
    res
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    players =
      for n <- String.split(Enum.at(flds, 0), ",") do
        String.to_integer(n)
      end

    trainers =
      for n <- String.split(Enum.at(flds, 1), ",") do
        String.to_integer(n)
      end

    "players = [" <> Mylib.intList_to_string(players) <> "], trainers = [" <> Mylib.intList_to_string(trainers) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.match_players_and_trainers(players, trainers)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
