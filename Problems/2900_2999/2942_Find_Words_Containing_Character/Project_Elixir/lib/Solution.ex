defmodule Solution do
  # 329ms - 357ms
  @spec find_words_containing(words :: [String.t], x :: char) :: [integer]
  def find_words_containing(words, x) do
    x_str = <<x>>
    Enum.reduce(words, {0, []}, fn word, {i, ans} ->
      if String.contains?(word, x_str) do
        {i + 1, ans ++ [i]}
      else
        {i + 1, ans}
      end
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    words = String.split(Enum.at(flds, 0), ",")
    x = Enum.at(String.to_charlist(Enum.at(flds, 1)), 0)
    "words = " <> Mylib.stringArray_to_string(words) <> ", x = " <> <<x>> |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_words_containing(words, x)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
