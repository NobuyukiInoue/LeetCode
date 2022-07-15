defmodule Solution do
  # 420ms - 621ms
  @spec reverse(x :: integer) :: integer
  def reverse(x) do
    helper(x, 0)
  end

  @spec helper(x :: integer, rev :: integer) :: integer
  def helper(x, rev) do
    cond do
      rev > 2147483648 or -2147483648 > rev ->
        0
      x != 0 ->
        helper(div(x, 10), rev*10 + rem(x, 10))
      true ->
        rev
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    x = temp |> String.to_integer()
    "x = " <> (x |> Integer.to_string()) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.reverse(x)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
