# 449ms - 526ms
defmodule Solution do
  @spec count_asterisks(s :: String.t) :: integer
  def count_asterisks(s) do
    s
    |> String.graphemes()
    |> Enum.reduce({false, 0}, fn c, {is_exclude, sum} ->
      case c do
        "|" -> {not is_exclude, sum}
        "*" -> {is_exclude, (is_exclude && sum) || sum + 1}
        _ -> {is_exclude, sum}
      end
    end)
    |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    s = String.replace(temp, "]", "")
    "s = " <> s |> IO.puts

    exectime = Benchmark.measure(fn ->
      result = Solution.count_asterisks(s)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
