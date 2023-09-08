defmodule Solution do
  # 294ms - 304ms
  @spec furthest_distance_from_origin(moves :: String.t) :: integer
  def furthest_distance_from_origin(moves) do
    {l, r, m} = Enum.reduce(String.codepoints(moves), {0, 0, 0}, fn move, {l, r, m} ->
      cond do
        move == "L" -> {l + 1, r, m}
        move == "R" -> {l, r + 1, m}
        true -> {l, r, m + 1}
      end
    end)
    if l >= r do
      l - r + m
    else
      r - l + m
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    moves = String.replace(temp, ", ", ",")
    "moves = \"" <> moves <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.furthest_distance_from_origin(moves)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
