defmodule Solution do
  # 274ms - 347ms
  @spec can_be_equal(s1 :: String.t, s2 :: String.t) :: boolean
  def can_be_equal(s1, s2) when s1 == s2 do
    true
  end

  def can_be_equal(s1, s2) do
    arr_s1 = String.codepoints(s1)
    {res, _} =
      Enum.reduce_while(0..1, {true, arr_s1}, fn i, {_, arr_s1} ->
        arr_s1 =
          if Enum.at(arr_s1, i) == String.at(s2, i + 2) do
            ch = Enum.at(arr_s1, i)
            temp = List.replace_at(arr_s1, i, Enum.at(arr_s1, i + 2))
            List.replace_at(temp, i + 2, ch)
          else
            arr_s1
          end
        if Enum.join(arr_s1) == s2 do
          {:halt, {true, arr_s1}}
        else
          {:cont, {false, arr_s1}}
        end
      end)
    res
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    s1 = Enum.at(flds, 0)
    s2 = Enum.at(flds, 1)
    "s1 = \"" <>  s1 <> "\", s2 = \"" <> s2 <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.can_be_equal(s1, s2)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
