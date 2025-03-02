defmodule Solution do
  # 6ms - 9ms
  @spec has_match(s :: String.t, p :: String.t) :: boolean
  def has_match(s, p) do
    helper_has_match(s, String.split(p, "*"))
  end

  @spec helper_has_match(s :: String.t, flds :: [String.t]) :: boolean
  def helper_has_match(s, _flds) when s == "" do
    false
  end

  def helper_has_match(s, [left_part | right_part]) when left_part == "" do
    if right_part == [] do
      true
    else
      helper_has_match(s, right_part)
    end
  end

  def helper_has_match(s, [left_part | right_part]) do
    res = :binary.match(s, left_part)
    cond do
      res == :nomatch ->
        false
      right_part == [""] ->
        true
      right_part == [] ->
        true
      true ->
        {pos, len} = res
        helper_has_match(String.slice(s, pos + len, String.length(s) - pos + len), right_part)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, ",")

    s = Enum.at(flds, 0)
    p = Enum.at(flds, 1)
    "s = \"" <> s <> "\", p = \"" <> p <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.has_match(s, p)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
