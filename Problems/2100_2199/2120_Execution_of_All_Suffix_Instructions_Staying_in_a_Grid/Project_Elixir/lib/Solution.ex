defmodule Solution do
  # 574ms - 618ms
  @spec execute_instructions(n :: integer, start_pos :: [integer], s :: String.t) :: [integer]
  def execute_instructions(n, start_pos, s) do
    execute_instructions(n, Enum.at(start_pos, 1), Enum.at(start_pos, 0), String.codepoints(s), []) |> Enum.reverse()
  end

  @spec execute_instructions(n :: integer, x :: integer, y :: integer, s :: [char], res :: [integer]) :: [integer]
  def execute_instructions(_, _, _, s, res) when s == [] do
    res
  end

  def execute_instructions(n, x, y, s, res) do
    execute_instructions(n, x, y, s |> tl, [helper(n, x, y, s) | res])
  end

  @spec helper(n :: integer, x :: integer, y :: integer, s :: [char]) :: integer
  def helper(n, x, y, s) do
    Enum.reduce_while(s, {x, y, 0}, fn inst, {x, y, cnt} ->
      {x, y} =
        cond do
          inst == "L" ->
            {x - 1, y}
          inst == "R" ->
            {x + 1, y}
          inst == "U" ->
            {x, y - 1}
          inst == "D" ->
            {x, y + 1}
        end
      if x < 0 or y < 0 or x == n or y == n do
        {:halt, {x, y, cnt}}
      else
        {:cont, {x, y, cnt + 1}}
      end
    end) |> elem(2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    n = String.to_integer(Enum.at(flds, 0))
    start_pos = for num <- String.split(Enum.at(flds, 1), ","), do: num |> String.trim() |> String.to_integer()
    s = Enum.at(flds, 2)
    "n = " <>  Integer.to_string(n) <> ", start_pos = [" <> Mylib.intList_to_string(start_pos) <> "], s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.execute_instructions(n, start_pos, s)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
