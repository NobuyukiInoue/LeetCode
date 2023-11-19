defmodule Solution do
  # 236ms - 283ms
  @spec find_words1(words :: [String.t]) :: [String.t]
  def find_words1(words) do
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    rowMap =
      Enum.reduce(rows, {0, Map.new()}, fn row, {i, rowMap} ->
        rowMap =
          Enum.reduce(String.to_charlist(row), rowMap, fn ch, rowMap ->
            Map.put(rowMap, ch - ?a, i)
          end)
        {i + 1, rowMap}
      end) |> elem(1)

    Enum.reduce(words, [], fn word, res ->
      word_lower = word |> String.downcase() |> String.to_charlist()
      row = Map.get(rowMap, (word_lower |> hd) - ?a)
      onSameRow =
        Enum.reduce_while(word_lower, true, fn ch, _ ->
          if Map.get(rowMap, ch - ?a) != row do
            {:halt, false}
          else
            {:cont, true}
          end
        end)
      if onSameRow do
        res ++ [word]
      else
        res
      end
    end)
  end

  # 237ms - 252ms
  @spec find_words(words :: [String.t]) :: [String.t]
  def find_words(words) do
    top = "qwertyuiop" |> String.graphemes |> MapSet.new
    middle = "asdfghjkl" |> String.graphemes |> MapSet.new
    bottom = "zxcvbnm" |> String.graphemes |> MapSet.new

    check_word = fn(word) ->
      as_set = word |> String.downcase
                    |> String.graphemes
                    |> MapSet.new

        MapSet.subset?(as_set, top) or MapSet.subset?(as_set, middle) or MapSet.subset?(as_set, bottom)
    end

    for word <- words, check_word.(word), do: word
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    words = String.split(temp, ",")

    "words = " <> Mylib.stringArray_to_string(words) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_words(words)
      "result = " <> Mylib.stringArray_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
