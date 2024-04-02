defmodule Solution do
  # 4391ms - 4402ms
  @spec remove_duplicates(s :: String.t, k :: integer) :: String.t
  def remove_duplicates(s, k) when length(s) < k do
    s
  end

  def remove_duplicates(s, k) do
    st =
      Enum.reduce(String.to_charlist(s), [], fn ch, st ->
        if Enum.count(st) > 0 and st |> hd |> hd == ch do
          [head | tail] = st
          [t_ch | [cnt | _]] = head
          if cnt + 1 == k do
            tail
          else
            [[t_ch, cnt + 1]] ++ tail
          end
        else
          [[ch, 1]] ++ st
        end
      end)
    |> Enum.reverse()
    Enum.reduce(st, "", fn cur, res ->
      [ch, cnt] = cur
      res <> String.duplicate(<<ch>>, cnt)
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    s = Enum.at(flds, 0)
    k = String.to_integer(Enum.at(flds, 1))
    "s = \"" <> s <> "\", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.remove_duplicates(s, k)
      "result = \"" <> result <> "\"" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
