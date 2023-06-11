defmodule Solution do
  # 630ms - 696ms
  @spec minimized_string_length(s :: String.t) :: integer
  def minimized_string_length(s) do
    s |>
    String.to_charlist |>
    Enum.reduce(%{}, fn x, acc -> Map.put(acc, x, 1) end) |>
    Enum.count
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimized_string_length(s)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
