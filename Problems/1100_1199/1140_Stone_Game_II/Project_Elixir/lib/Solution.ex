defmodule Solution do
  # 404ms - 419ms
  @spec stone_game_ii(piles :: [integer]) :: integer
  def stone_game_ii(piles) when piles == [] do
    0
  end

  def stone_game_ii(piles) do
    len_piles = Enum.count(piles)
    dp =
      for _ <- 0..len_piles do
        for _ <- 0..len_piles do 0 end
      end
    rev_piles = Enum.reverse(piles)
    {suffixSum, _} =
      Enum.reduce(Enum.slice(rev_piles, 1..len_piles), {[rev_piles |> hd], rev_piles |> hd}, fn rev_pile, {suffixSum, prev} ->
        {[rev_pile + prev | suffixSum], rev_pile + prev}
      end)
    helper(piles, dp, suffixSum, 0, 1) |> elem(0)
  end

  @spec helper(piles :: [integer], dp :: [[integer]], suffxSum :: [integer], i :: integer, m :: integer) :: {integer, [integer]}
  def helper(piles, dp, _suffixSum, _i, _m) when piles == [] do
    {0, dp}
  end

  def helper(piles, dp, suffixSum, i, m) do
    if i + 2*m >= Enum.count(piles) do
      {Enum.at(suffixSum, i), dp}
    else
      if Enum.at(Enum.at(dp, i), m) != 0 do
        {Enum.at(Enum.at(dp, i), m), dp}
      else
        {result, dp} = Enum.reduce(1..2*m, {0, dp}, fn x, {result, dp} ->
          {res, dp} = helper(piles, dp, suffixSum, i + x, max(m, x))
          {max(result, Enum.at(suffixSum, i) - res), dp}
        end)
        {result, List.replace_at(dp, i, List.replace_at(Enum.at(dp, i), m, result))}
      end
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    piles = for n <- String.split(flds, ",") do String.to_integer(n) end
    "piles = [" <> Mylib.intList_to_string(piles) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.stone_game_ii(piles)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
