use Bitwise

defmodule Solution do
  # 605ms - 618ms
  @spec sum_game(num :: String.t) :: boolean
  def sum_game(num) do
    sum_game(String.to_charlist(num), 0, String.length(num), 0.0)
  end
  @spec sum_game(num :: [char], pos :: integer, len_num :: integer, res :: float) :: boolean
  def sum_game(num, pos, len_num, res) do
    if num != [] do
      ch = Enum.at(num, 0)
      if pos < div(len_num, 2) do
        if ch == ?? do
          sum_game(num |> tl, pos + 1, len_num, res + 4.5)
        else
          sum_game(num |> tl, pos + 1, len_num, res + ((ch) -?0))
        end
      else
        if ch == ?? do
          sum_game(num |> tl, pos + 1, len_num, res - 4.5)
        else
          sum_game(num |> tl, pos + 1, len_num, res - ((ch) -?0))
        end
      end
    else
      res != 0
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    num = String.replace(temp, ", ", ",")
    "num = " <> num |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sum_game(num)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
