defmodule Solution do
  # 287ms
  @spec climb_stairs(n :: integer) :: integer
  def climb_stairs(n), do: do_climb_stairs(n, 1, 0, 1)
  defp do_climb_stairs(n, n, a, b), do: a + b
  defp do_climb_stairs(n, step, a, b), do: do_climb_stairs(n, step + 1, b, a + b)

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    n = temp |> String.to_integer()
    "n = " <>  Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.climb_stairs(n)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
