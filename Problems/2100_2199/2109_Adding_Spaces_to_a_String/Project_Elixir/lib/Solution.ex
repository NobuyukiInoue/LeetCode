defmodule Solution do
  # 849ms - 979ms
  @spec add_spaces(s :: String.t, spaces :: [integer]) :: String.t
  def add_spaces(s, spaces) do
    helper(String.graphemes(s), 0, spaces, []) |> Enum.join()
  end

  @spec helper(lst :: [String.t], ct :: integer, spaces :: [integer], ans :: [String.t]) :: String.t
  def helper([x | xs], ct, [space | rest] = spaces, ans) do
    if ct == space do
      helper(xs, ct + 1, rest, [x, " " | ans])
    else
      helper(xs, ct + 1, spaces, [x | ans])
    end
  end

  def helper([], _ct, _spaces, ans) do
    Enum.reverse(ans)
  end

  def helper(lst, _, [], ans) do
    Enum.concat([Enum.reverse(ans), lst])
  end

  # Time Limit Exceeded.(55/66)
  @spec add_spaces_bad(s :: String.t, spaces :: [integer]) :: String.t
  def add_spaces_bad(s, spaces) do
    {res, pre} =
    Enum.reduce(spaces, {"", 0}, fn pos, {res, pre} ->
      res =
        if pos == 0 do
          " "
        else
          res <> String.slice(s, pre..pos-1) <> " "
        end
      pre = pos
      {res, pre}
    end)
    res <> String.slice(s, pre..-1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, "],[")

    s = Enum.at(flds, 0)
    spaces = for num <- String.split(Enum.at(flds, 1), ",") do String.to_integer(num) end
    "s = \"" <> s <> "\", spaces = " <> Mylib.stringArray_to_string(spaces) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.add_spaces(s, spaces)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
