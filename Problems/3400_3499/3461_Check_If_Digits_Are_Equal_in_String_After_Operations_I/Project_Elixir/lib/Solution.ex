defmodule Solution do
  # 784ms - 826ms
  @spec has_same_digits(s :: String.t) :: boolean
  def has_same_digits(s) do
    if String.length(s) == 2 do
      String.at(s, 0) == String.at(s, 1)
    else
      has_same_digits(helper(s))
    end
  end

  @spec helper(s :: String.t) :: String.t
  def helper(s) do
    Enum.reduce_while(String.to_charlist(s), {0, ""}, fn ch, {i, new_s} ->
      if i == String.length(s) - 1 do
        {:halt, {i + 1, new_s}}
      else
        {:cont, {i + 1, new_s <> Integer.to_string(rem(ch - ?0 + String.to_integer(String.at(s, i + 1)), 10))}}
      end
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.has_same_digits(s)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
