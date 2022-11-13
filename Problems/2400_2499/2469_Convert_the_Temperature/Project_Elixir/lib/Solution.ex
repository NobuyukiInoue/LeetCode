defmodule Solution do
  @spec convert_temperature(celsius :: float) :: [float]
  # 335ms - 438ms
  def convert_temperature(celsius) do
    [celsius + 273.15, celsius * 1.80 + 32.00]
  end

  @spec floatList_to_string(nums :: [float]) :: String.t
  def floatList_to_string(nums) do
    Enum.join(nums, ", ")
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")
    celsius = String.to_float(flds)
    "celsius = " <> Float.to_string(celsius) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.convert_temperature(celsius)
      "result = [" <> floatList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
