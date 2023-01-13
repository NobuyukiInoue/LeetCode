defmodule Solution do
  # 302ms
  @spec count_digits(num :: integer) :: integer
  def count_digits(num) do
    count_digits(num, num, 0)
  end

  @spec count_digits(num :: integer, n :: integer, ans :: integer) :: integer
  def count_digits(_, 0, ans) do
    ans
  end

  def count_digits(num, n, ans) do
    if rem(num, rem(n, 10)) == 0 do
      count_digits(num, div(n, 10), ans + 1)
    else
      count_digits(num, div(n, 10), ans)
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
      result = Solution.count_digits(num)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
