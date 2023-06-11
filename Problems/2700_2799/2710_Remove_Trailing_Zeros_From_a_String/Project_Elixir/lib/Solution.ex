defmodule Solution do
  # 344ms
  @spec remove_trailing_zeros(num :: String.t) :: String.t
  def remove_trailing_zeros(num) do
    String.trim(num, "0")
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    num = String.replace(temp, ", ", ",")
    "num = \"" <> num <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.remove_trailing_zeros(num)
      "result = \"" <> result <> "\""|> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
