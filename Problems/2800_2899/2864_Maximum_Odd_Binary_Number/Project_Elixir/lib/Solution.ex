defmodule Solution do
  # 293ms - 305ms
  @spec maximum_odd_binary_number(s :: String.t) :: String.t
  def maximum_odd_binary_number(s) do
    cnts = (s |> to_charlist |> Enum.filter(&(&1 == ?1)) |> length)
    if cnts > 1 do
      String.duplicate("1", cnts - 1) <> String.duplicate("0", String.length(s) - cnts) <> "1"
    else
      String.duplicate("0", String.length(s) - cnts) <> "1"
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
      result = Solution.maximum_odd_binary_number(s)
      "result = \"" <> result <> "\""|> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
