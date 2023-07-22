defmodule Solution do
  # 307ms - 364ms
  @spec maximum_number_of_string_pairs(words :: [String.t]) :: integer
  def maximum_number_of_string_pairs(words) do
    Enum.reduce(words, {0, []}, fn word, {ans, word_set} ->
      if Enum.find(word_set, fn x -> x == word end) != nil do
        {ans + 1, word_set}
      else
        {ans, [String.reverse(word) | word_set]}
      end
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, ", ", ",")
    words = String.split(temp, ",")
    "words = " <> Mylib.stringArray_to_string(words) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.maximum_number_of_string_pairs(words)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
