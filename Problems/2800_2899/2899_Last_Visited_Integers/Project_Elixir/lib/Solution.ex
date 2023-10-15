defmodule Solution do
  # 285ms - 290ms
  def last_visited_integers(words) do
    Enum.reduce(words, {0, [], []}, fn word, {count, st, ans} ->
      if word == "prev" do
        len_st = Enum.count(st)
        count = count + 1
        if count <= len_st do
          {count, st, ans ++ [Enum.at(st, len_st - count)]}
        else
          {count, st, ans ++ [-1]}
        end
      else
        {0, st ++ [String.to_integer(word)], ans}
      end
    end) |> elem(2)
  end

  # 338ms - 365ms
  @spec last_visited_integers2(words :: [String.t]) :: [integer]
  def last_visited_integers2(words) do
    Enum.reduce(words, {0, [0], [0]}, fn word, {count, st, ans} ->
      "word = " <> word <> ", count = " <> Integer.to_string(count) |> IO.puts()
      "st = " <> Mylib.intList_to_string(st) |> IO.puts()
      "ans = " <> Mylib.intList_to_string(ans) |> IO.puts()
      if word == "prev" do
        len_st = Enum.count(st)
        if count + 1 <= len_st - 1 do
          {count + 1, st, [Enum.at(st, count) | ans]}
        else
          {count + 1, st, [-1 | ans]}
        end
      else
        {0, [String.to_integer(word) | st], ans}
      end
    end) |> elem(2) |> Enum.reverse() |> tl
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
      result = Solution.last_visited_integers(words)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
