defmodule Solution do
  # 317ms - 331ms
  @spec find_delayed_arrival_time(arrival_time :: integer, delayed_time :: integer) :: integer
  def find_delayed_arrival_time(arrival_time, delayed_time) do
    rem(arrival_time + delayed_time, 24)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    arrival_time = Enum.at(flds, 0) |> String.to_integer()
    delayed_time = Enum.at(flds, 1) |> String.to_integer()
    "arrival_time = " <> Integer.to_string(arrival_time) <>  ", delayed_time = " <> Integer.to_string(delayed_time) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_delayed_arrival_time(arrival_time, delayed_time)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
