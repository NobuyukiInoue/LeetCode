defmodule Solution do
  # 3ms - 7ms
  @spec is_balanced(num :: String.t) :: boolean
  def is_balanced(num) do
    Enum.reduce(String.to_charlist(num), {0, 1}, fn ch, {v_sum, sign} ->
      {v_sum + sign*(ch - ?0), -sign}
    end)
    |> elem(0) == 0
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    num = String.replace(temp, ", ", ",")
    "num = \"" <> num <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_balanced(num)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
