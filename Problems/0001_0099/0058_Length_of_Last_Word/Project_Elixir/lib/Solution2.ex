defmodule Solution2 do
  # 260ms - 300ms
  @spec length_of_last_word(s :: String.t) :: integer
  def length_of_last_word(s) do
    s
    |> String.to_charlist()
    |> process(true, 0)
  end

  defp process([], _, count), do: count
  defp process([?\s | tail], _restart, count), do: process(tail, true, count)
  defp process([_ | tail], true, _count), do: process(tail, false, 1)
  defp process([_ | tail], false, count), do: process(tail, false, count + 1)

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    s = String.replace(temp, "\"", "")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.length_of_last_word(s)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
