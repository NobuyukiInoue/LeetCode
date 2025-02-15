defmodule Solution do
  # 3ms - 4ms
  @spec possible_string_count(word :: String.t) :: integer
  def possible_string_count(word) do
    arr_word = String.codepoints(word)
    Enum.reduce(arr_word, {0, arr_word |> hd}, fn ch, {ans, prev} ->
      if ch == prev do
        {ans + 1, ch}
      else
        {ans, ch}
      end
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    word = String.replace(temp, ", ", ",")
    "word = \"" <> word <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.possible_string_count(word)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
