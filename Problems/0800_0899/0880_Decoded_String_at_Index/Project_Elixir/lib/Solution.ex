defmodule Solution do
  # Wrong Answer 29/45
  @spec decode_at_index(s :: String.t, k :: integer) :: String.t
  def decode_at_index(s, k) do
    arr_s = String.to_charlist(s)
    {i, tape_length} =
      Enum.reduce_while(arr_s, {0, 0}, fn ch, {i, tape_length} ->
        tape_length =
        if (?0 <= ch) and (ch <= ?9) do
          tape_length*(ch - ?0)
        else
          tape_length + 1
        end
        if k <= tape_length do
          {:halt, {i, tape_length}}
        else
          {:cont, {i + 1, tape_length}}
        end
      end)
    ch =
      Enum.reduce_while(i..0, {'', tape_length, k}, fn j, {_, tape_length, k} ->
        ch = Enum.at(arr_s, j)
        if (?0 <= ch) and (ch <= ?9) do
          tape_length = div(tape_length, ch - ?0)
          {:cont, {ch, tape_length, rem(k, tape_length)}}
        else
          if k == tape_length || k == 0 do
            {:halt, {ch, tape_length, k}}
          else
            {:cont, {ch, tape_length - 1, k}}
          end
        end
      end) |> elem(0)
    << ch >>
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, "],[")

    s = Enum.at(flds, 0)
    k = Enum.at(flds, 1) |> String.to_integer()
    "s = \"" <> s <> "\", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.decode_at_index(s, k)
      "result = \"" <> result <> "\"" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
