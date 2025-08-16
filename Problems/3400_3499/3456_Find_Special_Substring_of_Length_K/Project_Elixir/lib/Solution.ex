defmodule Solution do
  # 7ms
  @spec has_special_substring(s :: String.t, k :: integer) :: boolean
  def has_special_substring(s, k) do
    arr_s = s |> String.to_charlist()
    {_i, count, _ch} =
      Enum.reduce_while(arr_s, {0, 0, arr_s |> hd}, fn ch, {i, count, pre_ch} ->
        cond do
          ch != pre_ch and count == k ->
            {:halt, {i + 1, count, ch}}
          ch != pre_ch ->
            {:cont, {i + 1, 1, ch}}
          true ->
            {:cont, {i + 1, count + 1, ch}}
        end
      end)
    count == k
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
      result = Solution.has_special_substring(s, k)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
