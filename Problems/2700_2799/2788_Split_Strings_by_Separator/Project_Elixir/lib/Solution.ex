defmodule Solution do
  # 306ms - 324ms
  @spec split_words_by_separator(words :: [String.t], separator :: char) :: [String.t]
  def split_words_by_separator(words, separator) do
    words
    |> Enum.reduce([], fn word, ans ->
      [Enum.reduce(String.split(word, <<separator>>), [], fn fld, ans ->
        if fld != "" do
          [fld | ans]
        else
          ans
        end
      end) | ans]
    end)
    |> Enum.flat_map(fn item -> item end)
    |> Enum.reverse
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    words = String.split(String.replace(Enum.at(flds, 0), "\"", ""), ",")
    separator = Enum.at(String.to_charlist(Enum.at(flds, 1)), 0)
    "words = " <> Mylib.stringArray_to_string(words) <> ", separator = '" <> <<separator>> <> "'"|> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.split_words_by_separator(words, separator)
      "result = " <> Mylib.stringArray_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
