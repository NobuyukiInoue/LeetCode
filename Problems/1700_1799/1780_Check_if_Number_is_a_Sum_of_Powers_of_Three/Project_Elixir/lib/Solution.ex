defmodule Solution do
  # 259ms - 276ms
  @spec check_powers_of_three(n :: integer) :: boolean
  def check_powers_of_three(n) when n == 0 do
    true
  end

  def check_powers_of_three(n) when rem(n, 3) == 2 do
    false
  end

  def check_powers_of_three(n) do
    check_powers_of_three(div(n, 3))
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    n =  String.to_integer(flds)
    "n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.check_powers_of_three(n)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
