defmodule Solution do
  # 0ms
  @spec check_divisibility(n :: integer) :: boolean
  def check_divisibility(n) do
    check_divisibility(n, 1, 0, n)
  end

  @spec check_divisibility(n :: integer, v_prd :: integer, v_sum :: integer, temp_n :: integer) :: boolean
  def check_divisibility(n, v_prd, v_sum, temp_n) when temp_n > 0 do
    m = rem(temp_n, 10)
    check_divisibility(n, v_prd*m, v_sum + m, div(temp_n, 10))
  end

  def check_divisibility(n, v_prd, v_sum, _temp_n) do
    rem(n, v_prd + v_sum) == 0
  end

  @spec loop_main(temp :: String.t) :: :ox
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")

    n = String.to_integer(flds)
    "n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.check_divisibility(n)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
