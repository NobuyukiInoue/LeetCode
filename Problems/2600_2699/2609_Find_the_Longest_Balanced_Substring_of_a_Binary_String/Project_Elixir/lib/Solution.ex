defmodule Solution do
  # 470ms - 476ms
  @spec find_the_longest_balanced_substring(s :: String.t) :: integer
  def find_the_longest_balanced_substring(s) do
    find_the_longest_balanced_substring(s, "01", 0)
  end

  @spec find_the_longest_balanced_substring(s :: String.t, temp :: String.t, res :: integer) :: integer
  def find_the_longest_balanced_substring(s, temp, res) do
    if String.length(temp) > String.length(s) do
      res
    else
      if String.contains?(s, temp) do
        find_the_longest_balanced_substring(s, "0" <> temp <> "1", String.length(temp))
      else
        find_the_longest_balanced_substring(s, "0" <> temp <> "1", res)
      end
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = " <> s |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_the_longest_balanced_substring(s)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
