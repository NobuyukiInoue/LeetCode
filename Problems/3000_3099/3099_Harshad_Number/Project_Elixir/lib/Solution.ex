defmodule Solution do
  # 268ms - 286ms
  @spec sum_of_the_digits_of_harshad_number(x :: integer) :: integer
  def sum_of_the_digits_of_harshad_number(x) do
    sum_digits = get_sum_digits(x, 0)
    if rem(x, sum_digits) == 0 do
      sum_digits
    else
      -1
    end
  end

  @spec get_sum_digits(x :: integer, sum_digits :: integer) :: integer
  def get_sum_digits(x, sum_digits) when x == 0 do
    sum_digits
  end

  def get_sum_digits(x, sum_digits) do
    get_sum_digits(div(x, 10), sum_digits + rem(x, 10))
  end

  @spec loop_main(temp :: String.t) :: :ox
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")

    x = String.to_integer(flds)
    "x = " <> Integer.to_string(x) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sum_of_the_digits_of_harshad_number(x)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
