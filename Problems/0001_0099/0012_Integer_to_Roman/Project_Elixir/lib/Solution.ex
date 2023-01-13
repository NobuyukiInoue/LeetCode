defmodule Solution do
  # 909ms - 988ms
  @spec int_to_roman(num :: integer) :: String.t
  def int_to_roman(num) do
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    int_to_roman(num, 0, values, romans, "")
  end

  @spec int_to_roman(num :: integer, i :: integer, values :: [integer], romans :: [String.t], result :: String.t) :: String.t
  def int_to_roman(num, i, values, romans, result) do
    if num > 0 do
      next_i = get_values_index(num, i, values)
      int_to_roman(num - Enum.at(values, next_i), next_i, values, romans, result <> Enum.at(romans, next_i))
    else
      result
    end
  end

  @spec get_values_index(num :: integer, i :: integer, values :: [integer]) :: integer
  def get_values_index(num, i, values) do
    if Enum.at(values, i) > num do
      get_values_index(num, i + 1, values)
    else
      i
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    num = temp |> String.to_integer()
    "num = " <> (num |> Integer.to_string()) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.int_to_roman(num)
      "result = " <> result |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
