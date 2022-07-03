defmodule Solution do
  # 570ms - 625ms
  @spec length_of_longest_substring(s :: String.t) :: integer
  def length_of_longest_substring("") do
    0
  end

  def length_of_longest_substring(s) do
    s
    |> :binary.bin_to_list()
    |> Enum.with_index()
    |> Enum.reduce({%{}, 0, 0}, fn {char, index}, {map, low_index, max_len} ->
      i = map[char]
      low_index = (i && max(i + 1, low_index)) || low_index
      map = Map.put(map, char, index)
      max_len = max(max_len, (index - low_index) + 1)

      {map, low_index, max_len}
    end)
    |> elem(2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    s = String.replace(temp, "\"", "")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.length_of_longest_substring(s)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
