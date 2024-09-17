defmodule Solution do
  # 270ms - 313ms
  @spec check_two_chessboards(coordinate1 :: String.t, coordinate2 :: String.t) :: boolean
  def check_two_chessboards(coordinate1, coordinate2) do
    {c1, c2} = {String.to_charlist(coordinate1), String.to_charlist(coordinate2)}
    {d1, d2} = {Enum.at(c1, 0) + Enum.at(c1, 1), Enum.at(c2, 0) + Enum.at(c2, 1)}
    rem(d1, 2) == rem(d2, 2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, "],[")

    coordinate1 = Enum.at(flds, 0)
    coordinate2 = Enum.at(flds, 1)
    "coordinate1 = \"" <> coordinate1 <> "\", coordinate2 = \"" <> coordinate2 <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.check_two_chessboards(coordinate1, coordinate2)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
