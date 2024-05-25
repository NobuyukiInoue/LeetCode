defmodule Solution do
  # 312ms - 356ms
  @spec is_valid(word :: String.t) :: boolean
  def is_valid(word) do
    cond do
      String.length(word) < 3 ->
        false
      String.contains?(word, "@") ->
        false
      String.contains?(word, "#") ->
        false
      String.contains?(word, "$") ->
        false
      true ->
        is_vowel_and_letter(String.downcase(word))
      end
  end

  @spec is_vowel_and_letter(word :: String.t) :: boolean()
  def is_vowel_and_letter(word) do
    Enum.reduce_while(String.to_charlist(word), {false, {false, false}}, fn ch, {_res, {is_vowel, is_letter}} ->
      {is_vowel, is_letter} =
      if String.contains?("aeiou", <<ch>>) do
        {true, is_letter}
      else
        if ?a < ch and ch <= ?z do
          {is_vowel, true}
        else
          {is_vowel, is_letter}
        end
      end
      if is_vowel and is_letter do
        {:halt, {true, {is_vowel, is_letter}}}
      else
        {:cont, {false, {is_vowel, is_letter}}}
      end
    end)
    |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    word = String.replace(temp, ", ", ",")
    "word = \"" <> word <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_valid(word)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
