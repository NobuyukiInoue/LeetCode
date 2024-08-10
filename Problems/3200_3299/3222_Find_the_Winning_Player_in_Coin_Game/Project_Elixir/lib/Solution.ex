defmodule Solution do
  # 356ms - 388ms
  @spec losing_player(x :: integer, y :: integer) :: String.t
  def losing_player(x, y) do
    losing_player(x, y, 0)
  end

  @spec losing_player(x :: integer, y :: integer, cnt :: integer) :: String.t
  def losing_player(x, y, cnt) when x == 0 or y < 4 do
    if rem(cnt, 2) == 1 do
      "Alice"
    else
      "Bob"
    end
  end

  def losing_player(x, y, cnt) do
    losing_player(x - 1, y - 4, cnt + 1)
  end

  @spec loop_main(temp :: String.t) :: :oy
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    x = String.to_integer(Enum.at(flds, 0))
    y = String.to_integer(Enum.at(flds, 1))
    "x = " <> Integer.to_string(x) <> ", y = " <> Integer.to_string(y) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.losing_player(x, y)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
