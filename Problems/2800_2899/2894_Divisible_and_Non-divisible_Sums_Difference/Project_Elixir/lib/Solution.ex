defmodule Solution do
  # 329ms - 334ms
  @spec difference_of_sums(n :: integer, m :: integer) :: integer
  def difference_of_sums(n, m) do
    div((1 + n)*n, 2) - (1 + div(n, m))*div(n, m)*m
  end

  # 285ms - 367ms
  def difference_of_sums2(n, m) do
    Enum.reduce(1..n, 0, fn i, res ->
      if rem(i, m) != 0 do
        res + i
      else
        res - i
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    n = Enum.at(flds, 0) |> String.to_integer()
    m = Enum.at(flds, 1) |> String.to_integer()
    "n = " <>  Integer.to_string(n) <> ", m = " <> Integer.to_string(m) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = difference_of_sums(n, m)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
