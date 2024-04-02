defmodule Solution do
  # 259ms
  @spec seconds_to_remove_occurrences(s :: String.t) :: integer
  def seconds_to_remove_occurrences(s) do
    Enum.reduce(String.to_charlist(s), {0, 0, 0, 0}, fn ch, {i, ans, prefix, prev} ->
      if ch == ?1 do
        ans = max(prev, i - prefix)
        if ans > 0 do
          {i + 1, ans, prefix + 1, ans + 1}
        else
          {i + 1, ans, prefix + 1, prev}
        end
      else
        {i + 1, ans, prefix, prev}
      end
    end)
    |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.seconds_to_remove_occurrences(s)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
