use Bitwise

defmodule Solution do
  # 315ms - 355ms
  @spec divide(dividend :: integer, divisor :: integer) :: integer
  def divide(_, 0), do: raise ArithmeticError, "divide by zero"
  def divide(dividend, divisor), do: raw_divide(dividend, divisor) |> clamp()
  defp raw_divide(dividend, divisor) when dividend < 0, do: -raw_divide(-dividend, divisor)
  defp raw_divide(dividend, divisor) when divisor < 0, do: -raw_divide(dividend, -divisor)
  defp raw_divide(dividend, divisor), do: dividend |> divrem(divisor) |> elem(0)
  defp divrem(divisor, divisor), do: {1, 0}
  defp divrem(dividend, divisor) when dividend < divisor, do: {0, dividend}
  defp divrem(dividend, divisor) do
    {quotient1, remainder1} = divrem(dividend >>> 1, divisor)
    {quotient2, remainder2} = case remainder1 + (dividend &&& 1) do
      ^divisor -> {quotient1 + 1, 0}
      remainder2 -> {quotient1, remainder2}
    end
    case remainder1 + remainder2 do
      remainder when remainder >= divisor ->
        {quotient1 + quotient2 + 1, remainder - divisor}
      remainder ->
        {quotient1 + quotient2, remainder}
    end
  end

  @max  0x7FFF_FFFF
  @min -0x8000_0000

  defp clamp(n) when n < @min, do: @min
  defp clamp(n) when n > @max, do: @max
  defp clamp(n), do: n

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, ",")

    dividend = String.to_integer(Enum.at(flds, 0))
    divisor = String.to_integer(Enum.at(flds, 1))
    "dividend = " <> Integer.to_string(dividend) <> ", divisor = " <>  Integer.to_string(divisor) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.divide(dividend, divisor)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
