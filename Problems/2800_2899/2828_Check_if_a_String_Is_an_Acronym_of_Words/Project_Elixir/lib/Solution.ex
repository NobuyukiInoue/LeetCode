defmodule Solution do
  # 412ms - 450ms
  @spec is_acronym(words :: [String.t], s :: String.t) :: boolean
  def is_acronym(words, s) do
    Enum.reduce(words, "", fn word, target ->
      target <> String.at(word, 0)
    end) == s
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    words = String.split(String.replace(Enum.at(flds, 0), "\"", ""), ",")
    s = Enum.at(flds, 1)
    "words = " <> Mylib.stringArray_to_string(words) <> ", s = '" <> s <> "'"|> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_acronym(words, s)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
