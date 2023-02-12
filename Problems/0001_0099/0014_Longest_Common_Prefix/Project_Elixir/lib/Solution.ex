defmodule Solution do
  # 340ms
  @spec longest_common_prefix(strs :: [String.t]) :: String.t
  def longest_common_prefix([first_str | remaining_strs]) do
    Enum.reduce(remaining_strs, first_str, fn str, prefix ->
        get_matching_prefix(str, prefix, "")
    end)
  end

  defp get_matching_prefix(<<match::binary-size(1), str1::binary>> =s1, <<match::binary-size(1), str2::binary>> = s2, prefix \\ "") when s1 != "" and s2 != "" do
      get_matching_prefix(str1, str2, prefix <> match)
  end

  defp get_matching_prefix(_, _, prefix), do: prefix

@spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    temp = String.replace(temp, "\"", "")
    strs = String.split(temp, ",")
    "strs = " <> Mylib.stringArray_to_string(strs) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.longest_common_prefix(strs)
      "result = \"" <> to_string(result) <> "\"" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
