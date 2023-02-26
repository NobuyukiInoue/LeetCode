defmodule Solution do
  # 298ms - 361ms
  @spec min_max_difference(num :: integer) :: integer
  def min_max_difference(num) do
    min_max_difference(Integer.to_string(num), 0)
  end

  @spec min_max_difference(num_str :: String.t, i :: integer) :: integer
  def min_max_difference(num_str, i) do
    if String.at(num_str, i) != "9" or i >= String.length(num_str) - 1 do
      String.to_integer(String.replace(num_str, String.at(num_str, i), "9")) - String.to_integer(String.replace(num_str, String.at(num_str, 0), "0"))
    else
      min_max_difference(num_str, i + 1)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    num = String.to_integer(flds)
    "num = " <> Integer.to_string(num) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.min_max_difference(num)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
