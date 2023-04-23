defmodule Solution do
  # 244ms - 277ms
  @spec greatest_letter(s :: String.t) :: String.t
  def greatest_letter(s) do
    greatest_letter(String.to_charlist(s), ?Z, ?z)
  end

  @spec greatest_letter(arr :: [char], capital :: integer, small :: integer) :: String.t
  def greatest_letter(arr, capital, small) when capital >= ?A do
    if Enum.find_index(arr, fn item -> item == capital end) do
      if Enum.find_index(arr, fn item -> item == small end) do
        <<capital>>
      else
        greatest_letter(arr, capital - 1, small - 1)
      end
    else
      greatest_letter(arr, capital - 1, small - 1)
    end
  end

  def greatest_letter(_, _, _) do
    ""
  end

  # 244ms - 268ms
  @spec greatest_letter_use_Map(s :: String.t) :: String.t
  def greatest_letter_use_Map(s) do
    set =
    s
    |> String.to_charlist()
    |> MapSet.new()

  ?Z..?A//-1
  |> Enum.reduce_while("", fn c, _ ->
    if MapSet.member?(set, c) && MapSet.member?(set, c + 32) do
      {:halt, List.to_string([c])}
    else
      {:cont, ""}
    end
  end)
  end

@spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = " <> s |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.greatest_letter(s)
      "result = \"" <> result <> "\""|> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
