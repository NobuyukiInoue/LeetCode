defmodule Solution do
  # 398ms - 401ms
  @spec maximum_xor_product(a :: integer, b :: integer, n :: integer) :: integer
  def maximum_xor_product(a, b, n) when n == 0 do
    rem(a*b, 1_000_000_007)
  end

  def maximum_xor_product(a, b, n) do
    {a, b} = Enum.reduce(0..n-1, {a, b}, fn i, {a, b} ->
      x = Bitwise.<<<(1, i)
      {t1, t2} = {Bitwise.bxor(a, x), Bitwise.bxor(b, x)}
      if t1*t2 > a*b do
        {t1, t2}
      else
        {a, b}
      end
    end)
    rem(a*b, 1_000_000_007)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    a = String.to_integer(Enum.at(flds, 0))
    b = String.to_integer(Enum.at(flds, 1))
    n = String.to_integer(Enum.at(flds, 2))
    "a = " <> Integer.to_string(a) <> ", b = " <> Integer.to_string(b) <> ", n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.maximum_xor_product(a, b, n)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
