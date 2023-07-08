defmodule Solution do
  # 482ms - 504ms
  @spec largest_merge(word1 :: String.t, word2 :: String.t) :: String.t
  def largest_merge(word1, word2) do
    largest_merge(String.codepoints(word1), String.codepoints(word2), "")
  end

  @spec largest_merge(word1 :: [char], word2 :: [char], ans :: String.t) :: String.t
  def largest_merge(word1, word2, ans) when word1 == [] or word2 == [] do
    ans <> to_string(word1) <> to_string(word2)
  end

  def largest_merge([h1 | t1], [h2 | t2], ans) when [h1 | t1] > [h2 | t2] do
    largest_merge(t1, [h2 | t2], ans <> h1)
  end

  def largest_merge([h1 | t1], [h2 | t2], ans) do
    largest_merge([h1 | t1], t2, ans <> h2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, "],[")

    word1 = Enum.at(flds, 0)
    word2 = Enum.at(flds, 1)
    "word1 = \"" <> word1 <> "\", word2 = \"" <> word2 <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.largest_merge(word1, word2)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
