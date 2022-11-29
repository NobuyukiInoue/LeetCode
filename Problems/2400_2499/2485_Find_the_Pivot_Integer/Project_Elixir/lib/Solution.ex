defmodule Solution do
  # 331ms - 435ms
  @spec pivot_integer(n :: integer) :: integer
  def pivot_integer(n) do
    pivot_integer(n, 1, 0, div(n*(n + 1), 2))
  end

  @spec pivot_integer(n :: integer, i :: integer, l_sum :: integer, r_sum :: integer) :: integer
  def pivot_integer(n, i, l_sum, r_sum) do
    if i > n do
      -1
    else
      if l_sum == r_sum - i do
        i
      else
        pivot_integer(n, i + 1, l_sum + i, r_sum - i)
      end
    end
  end

  # 463ms - 550ms
  @spec pivot_integer2(n :: integer) :: integer
  def pivot_integer2(n) do
    x = :math.sqrt((n * n + n) / 2)
    if ceil(x) == trunc(x) do
      trunc(x)
    else
      -1
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    n = String.to_integer(flds)
    "n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.pivot_integer(n)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
