defmodule Solution do
  # 0ms
  @spec smallest_number(n :: integer, t :: integer) :: integer
  def smallest_number(n, t) do
    if rem(get_prod(n, 1), t) == 0 do
      n
    else
      smallest_number(n + 1, t)
    end
  end

  @spec get_prod(n :: integer, prod :: integer) :: integer
  def get_prod(n, prod) when n == 0 do
    prod
  end

  def get_prod(n, prod) do
    get_prod(div(n, 10), prod*rem(n, 10))
  end

  @spec loop_main(temp :: String.t) :: :ot
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    n = String.to_integer(Enum.at(flds, 0))
    t = String.to_integer(Enum.at(flds, 1))
    "n = " <> Integer.to_string(n) <> ", t = " <> Integer.to_string(t) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.smallest_number(n, t)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
