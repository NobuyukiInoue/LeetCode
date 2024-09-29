defmodule Solution do
  # 14ms - 16ms
  @spec longest_nice_substring(s :: String.t) :: String.t
  def longest_nice_substring(s) when s == "" do
    ""
  end

  def longest_nice_substring(s) do
    arr_s = String.to_charlist(s)
    ss =
      Enum.reduce(arr_s, MapSet.new(), fn ch, ss ->
        MapSet.put(ss, ch)
      end)
    Enum.reduce_while(arr_s, {0, s}, fn ch, {i, s} ->
      if not MapSet.member?(ss, to_upper(ch)) or not MapSet.member?(ss, to_lower(ch)) do
        s0 = longest_nice_substring(String.slice(s, 0, i))
        s1 = longest_nice_substring(String.slice(s, i+1, String.length(s) - 1))
        if String.length(s0) >= String.length(s1) do
          {:halt, {i + 1, s0}}
        else
          {:halt, {i + 1, s1}}
        end
      else
        {:cont, {i + 1, s}}
      end
    end) |> elem(1)
  end

  @spec to_lower(ch :: char()) :: char()
  def to_lower(ch) do
    if ?A <= ch and ch <= ?Z do
      ch + (?a - ?A)
    else
      ch
    end
  end

  @spec to_upper(ch :: char()) :: char()
  def to_upper(ch) do
    if ?a <= ch and ch <= ?z do
      ch - (?a - ?A)
    else
      ch
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.longest_nice_substring(s)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
