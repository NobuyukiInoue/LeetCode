defmodule Solution do
  # 506ms - 509ms
  @spec maximum_subsequence_count(text :: String.t, pattern :: String.t) :: integer
  def maximum_subsequence_count(text, pattern) do
    {p0, p1} = {String.at(pattern, 0), String.at(pattern, 1)}
    {res, cnt1, cnt2} =
      Enum.reduce(String.codepoints(text), {0, 0, 0}, fn ch, {res, cnt1, cnt2} ->
        {res, cnt2} =
        if ch == p1 do
          {res + cnt1, cnt2 + 1}
        else
          {res, cnt2}
        end
        cnt1 =
        if ch == p0 do
          cnt1 + 1
        else
          cnt1
        end
        {res, cnt1, cnt2}
      end)
    res + max(cnt1, cnt2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    text = Enum.at(flds, 0)
    pattern = Enum.at(flds, 1)
    "text = \"" <> text <> "\", pattern = \"" <> pattern <> "\"" |> IO.puts()

    execright = Benchmark.measure(fn ->
      result = Solution.maximum_subsequence_count(text, pattern)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(execright, 3)) <> " [s]\n" |> IO.puts()
  end
end
