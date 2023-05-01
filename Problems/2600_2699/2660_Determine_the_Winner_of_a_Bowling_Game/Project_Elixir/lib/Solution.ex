defmodule Solution do
  # 432ms - 458ms
  @spec is_winner(player1 :: [integer], player2 :: [integer]) :: integer
  def is_winner(player1, player2) do
    score1 = get_score(player1)
    score2 = get_score(player2)
    cond do
      score1 > score2 -> 1
      score1 < score2 -> 2
      true -> 0
    end
  end

  @spec get_score(nums :: [integer]) :: integer, integer
  def get_score(nums) do
    nums |>
    Enum.reduce({0, 0}, fn num, {score, cnt} ->
      {score, cnt} =
      if cnt > 0 do
        {score + num*2, cnt - 1}
      else
        {score + num, cnt}
      end
      if num == 10 do
        {score, 2}
      else
        {score, cnt}
      end
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    player1 = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    player2 = for num <- String.split(Enum.at(flds, 1), ","), do: num |> String.trim() |> String.to_integer()
    "player1 = [" <>  Mylib.intList_to_string(player1) <> "], player2 = [" <> Mylib.intList_to_string(player2) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_winner(player1, player2)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
