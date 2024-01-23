defmodule Solution do
  # 440ms - 451ms
  @spec min_moves_to_capture_the_queen(a :: integer, b :: integer, c :: integer, d :: integer, e :: integer, f :: integer) :: integer
  def min_moves_to_capture_the_queen(a, b, c, d, e, f) do
    cond do
      a == e and not (a == c and d > min(b,f) and d < max(b,f)) -> 1
      b == f and not (b == d and c > min(a,e) and c < max(a,e)) -> 1
      c + d == e + f and not (c + d == a + b and a > min(c , e) and a < max(c, e)) -> 1
      c - d == e - f and not (c - d == a - b and a > min(c , e) and a < max(c, e)) -> 1
      true -> 2
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")
    a = String.to_integer(Enum.at(flds, 0))
    b = String.to_integer(Enum.at(flds, 1))
    c = String.to_integer(Enum.at(flds, 2))
    d = String.to_integer(Enum.at(flds, 3))
    e = String.to_integer(Enum.at(flds, 4))
    f = String.to_integer(Enum.at(flds, 5))

    "a = " <> Integer.to_string(a) <> ", b = " <> Integer.to_string(b) <> ", c = " <> Integer.to_string(c) <> ", d = " <> Integer.to_string(d) <> ", e = " <> Integer.to_string(e) <> ", f = " <> Integer.to_string(f) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.min_moves_to_capture_the_queen(a, b, c, d, e, f)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
