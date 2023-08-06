defmodule Solution do
  # 382ms - 401ms
  @spec vowel_strings(words :: [String.t], left :: integer, right :: integer) :: integer
  def vowel_strings(words, left, right) do
    vowel_strings(words, left, right, 0, 0)
  end

  @spec vowel_strings(words :: [String.t], left :: integer, right :: integer, index :: integer, count :: integer) :: integer
  def vowel_strings([head | tail], left, right, index, count) when index >= left and index <= right do
    if String.contains?("aeiou", String.at(head, 0)) and String.contains?("aeiou", String.at(head, String.length(head) - 1)) do
      vowel_strings(tail, left, right, index + 1, count + 1)
    else
      vowel_strings(tail, left, right, index + 1, count)
    end
  end

  def vowel_strings([_ | tail], left, right, index, count) do
    vowel_strings(tail, left, right, index + 1, count)
  end

  def vowel_strings([], _, _, _, count) do
    count
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    words = String.split(String.replace(Enum.at(flds, 0), "\"", ""), ",")
    left = Enum.at(flds, 1) |> String.to_integer()
    right = Enum.at(flds, 2) |> String.to_integer()
    "words = " <> Mylib.stringArray_to_string(words) <> ", left = " <> Integer.to_string(left) <> ", right = " <> Integer.to_string(right) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.vowel_strings(words, left, right)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
