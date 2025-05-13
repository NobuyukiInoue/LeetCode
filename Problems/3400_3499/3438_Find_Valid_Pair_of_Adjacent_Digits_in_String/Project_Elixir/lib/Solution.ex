defmodule Solution do
  # 15ms - 26ms
  @spec find_valid_pair(s :: String.t) :: String.t
  def find_valid_pair(s) do
    arr_s = s |> String.codepoints()
    cnts =
      Enum.reduce(arr_s , %{}, fn ch, cnts ->
        Map.put(cnts, ch, Map.get(cnts, ch, 0) + 1)
      end)

    {_i, ans} =
      Enum.reduce_while(arr_s, {0, ""}, fn ch, {i, _ans} ->
        if i == 0 do
          {:cont, {i + 1, ""}}
        else
          ch_p = Enum.at(arr_s, i - 1)
          if ch_p != ch and cnts[ch_p] == String.to_integer(ch_p) and cnts[ch] == String.to_integer(ch) do
            {:halt, {i + 1, ch_p <> ch}}
          else
            {:cont, {i + 1, ""}}
          end
        end
      end)
    if ans != "" do
      ans
    else
      ""
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_valid_pair(s)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
