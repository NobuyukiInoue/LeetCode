defmodule Solution do
  # 284ms - 329ms
  @spec maximum_length_substring(s :: String.t) :: integer
  def maximum_length_substring(s) do
    arr_s = String.to_charlist(s)
    Enum.reduce(arr_s, {0, 0, %{}, 0}, fn ch, {i, j, freq, ans} ->
      freq = Map.put(freq, ch, Map.get(freq, ch, 0) + 1)
      {j, freq} = is_freq_3(arr_s, freq, ch, j)
      {i + 1, j, freq, max(ans, i - j + 1) }
    end)
    |> elem(3)
  end

  def is_freq_3(arr_s, freq, ch, j) do
    if freq[ch] != 3 do
      {j, freq}
    else
      ch_j = Enum.at(arr_s, j)
      is_freq_3(arr_s, Map.put(freq, ch_j, freq[ch_j] - 1), ch, j + 1)
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
      result = Solution.maximum_length_substring(s)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
