defmodule Solution do
  # 281ms - 294ms
  @spec alternate_digit_sum(n :: integer) :: integer
  def alternate_digit_sum(n) do
    alternate_digit_sum(n, 1, 0, 0)
  end

  @spec alternate_digit_sum(n :: integer, sign :: integer, cnt :: integer, ans :: integer) :: integer
  def alternate_digit_sum(n, sign, cnt, ans) when n > 0 do
    alternate_digit_sum(div(n, 10), sign*-1, cnt + 1, ans + sign*rem(n, 10))
  end

  def alternate_digit_sum(_, _, cnt, ans) when rem(cnt, 2) == 1 do
    ans
  end

  def alternate_digit_sum(_, _, _, ans) do
    -ans
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    n = String.to_integer(flds)
    "n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.alternate_digit_sum(n)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
