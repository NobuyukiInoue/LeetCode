defmodule Solution do
  # 295ms - 345ms
  @spec get_longest_subsequence(words :: [String.t], groups :: [integer]) :: [String.t]
  def get_longest_subsequence(words, groups) do
    Enum.zip(words, groups)
    |> tl
    |> Enum.reduce({groups |> hd, [words |> hd]}, fn {w, g}, {pre_group, ans} ->
      if g == pre_group do
        {g, ans}
      else
        {g, [w] ++ ans}
      end
    end)
    |> elem(1)
    |> Enum.reverse()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    words = String.split(Enum.at(flds, 0), ",")
    groups = for num <- String.split(Enum.at(flds, 1), ","), do: num |> String.trim() |> String.to_integer()
    "words = " <> Mylib.stringArray_to_string(words) <> ", groups = [" <> Mylib.intList_to_string(groups) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.get_longest_subsequence(words, groups)
      "result = " <> Mylib.stringArray_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
