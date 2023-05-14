defmodule Solution do
  # 232ms - 254ms
  @spec length_of_last_word(s :: String.t) :: integer
  def length_of_last_word(s) do
    s
    |> String.split
    |> List.last
    |> String.length
  end

  # 256ms - 264ms
  @spec length_of_last_word2(s :: String.t) :: integer
  def length_of_last_word2(s) do
    s = String.trim(s)
    i =
    Enum.reduce_while(String.to_charlist(String.reverse(s)), String.length(s) - 1, fn ch, i ->
      if i >= 0 and ch != ?\s do
        {:cont, i - 1}
      else
        {:halt, i}
      end
    end)
    String.length(s) - 1 - i
  end

  # 272ms - 279ms
  @spec length_of_last_word3(s :: String.t) :: integer
  def length_of_last_word3(s) do
    s = String.trim(s)
    i =
    Enum.reduce_while(String.codepoints(String.reverse(s)), String.length(s) - 1, fn ch, i ->
      if i >= 0 and ch != " " do
        {:cont, i - 1}
      else
        {:halt, i}
      end
    end)
    String.length(s) - 1 - i
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    s = String.replace(temp, "\"", "")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.length_of_last_word(s)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
