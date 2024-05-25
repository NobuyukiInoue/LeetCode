defmodule Solution do
  # 329ms - 377ms
  @spec number_of_special_chars(word :: String.t) :: integer
  def number_of_special_chars(word) do
    Enum.reduce(String.codepoints(word), %{}, fn ch, cnts ->
      if ch >= "a" and String.contains?(word, String.upcase(ch)) do
        Map.put(cnts, ch, true)
      else
        cnts
      end
    end)
    |> map_size()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    word = String.replace(temp, ", ", ",")
    "word = \"" <> word <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.number_of_special_chars(word)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
