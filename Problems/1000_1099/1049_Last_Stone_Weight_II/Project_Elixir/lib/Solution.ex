defmodule Solution do
  # 443ms - 459ms
  @spec last_stone_weight_ii(stones :: [integer]) :: integer
  def last_stone_weight_ii(stones) do
    if Enum.count(stones) == 1 do
      stones |> hd
    else
      total = Enum.sum(stones)
      half = div(total, 2)
      dp = for _ <- 0..half, do: false
      dp = List.replace_at(dp, 0, true)
      dp =
        Enum.reduce(stones, dp, fn stone, dp ->
          Enum.reduce(half..stone, dp, fn j, dp ->
            if Enum.at(dp, j - stone) do
              List.replace_at(dp, j, true)
            else
              dp
            end
          end)
        end)
      i =
        Enum.reduce_while(half..0, 0, fn i, _ ->
          if Enum.at(dp, i) == false do
            {:cont, i}
          else
            {:halt, i}
          end
        end)
      total - 2*i
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    stones = for n <- String.split(flds, ",") do String.to_integer(n) end
    "stones = [" <> Mylib.intList_to_string(stones) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.last_stone_weight_ii(stones)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
