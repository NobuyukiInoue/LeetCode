defmodule Solution do
  # 325ms - 361ms
  @spec my_sqrt(x :: integer) :: integer
  def my_sqrt(x) when x == 0 do
    0
  end

  def my_sqrt(x) do
    helper(x, 1, x, 0)
  end

  @spec helper(x :: integer, left :: integer, right :: integer, ans :: integer) :: integer
  def helper(x, left, right, ans) when left <= right do
		mid = left + div(right - left, 2)
		if mid <= div(x, mid) do
      helper(x, mid + 1, right, mid)
		else
      helper(x, left, mid - 1, ans)
    end
  end

  def helper(_, _, _, ans) do
    ans
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")
    x = String.to_integer(flds)
    "x = " <> to_string(x) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.my_sqrt(x)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
