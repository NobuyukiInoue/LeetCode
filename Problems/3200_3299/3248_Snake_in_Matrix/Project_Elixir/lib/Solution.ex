defmodule Solution do
  # 360ms - 387ms
  @spec final_position_of_snake(n :: integer, commands :: [String.t]) :: integer
  def final_position_of_snake(n, commands) do
    {x, y} =
      Enum.reduce(commands, {0, 0}, fn cmd, {x, y} ->
        case cmd do
          "LEFT" ->
            {x, y - 1}
          "RIGHT" ->
            {x, y + 1}
          "UP" ->
            {x - 1, y}
          _ ->
            {x + 1, y}
        end
      end)
      x*n + y
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, "],[")

    n = String.to_integer(Enum.at(flds, 0))
    commands = String.split(Enum.at(flds, 1), ",")
    "n = " <> Integer.to_string(n) <> ", commands = " <> Mylib.stringArray_to_string(commands) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.final_position_of_snake(n, commands)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
