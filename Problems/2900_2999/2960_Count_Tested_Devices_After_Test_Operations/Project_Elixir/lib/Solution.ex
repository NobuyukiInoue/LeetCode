defmodule Solution do
  # 270ms - 278ms
  @spec count_tested_devices(battery_percentages :: [integer]) :: integer
  def count_tested_devices(battery_percentages) do
    Enum.reduce(battery_percentages, 0, fn target, ans ->
      if target > ans do; ans + 1 else ans end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    battery_percentages = for n <- String.split(flds, ",") do String.to_integer(n) end
    "battery_percentages = [" <> Mylib.intList_to_string(battery_percentages) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_tested_devices(battery_percentages)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
