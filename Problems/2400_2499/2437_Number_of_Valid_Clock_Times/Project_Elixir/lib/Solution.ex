# 418ms - 484ms
defmodule Solution do
  @spec count_time(time :: String.t()) :: integer
  def count_time(time) do
    [hh, mm] = String.split(time, ":") |> Enum.map(&String.to_charlist/1)
    count_hh(hh) * count_mm(mm)
  end

  def count_hh([??, ??]), do: 24

  def count_hh([??, h]) do
    if h in ?0..?3, do: 3, else: 2
  end

  def count_hh([?2, ??]), do: 4
  def count_hh([_, ??]), do: 10
  def count_hh(_), do: 1

  def count_mm([??, ??]), do: 60
  def count_mm([??, _]), do: 6
  def count_mm([_, ??]), do: 10
  def count_mm(_), do: 1

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[", "")
    time = String.replace(temp, "]", "")
    "time = " <> time |> IO.puts

    exectime = Benchmark.measure(fn ->
      result = Solution.count_time(time)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
