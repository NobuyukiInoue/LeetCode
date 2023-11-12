defmodule Solution do
  # 277ms - 294ms
  @spec distribute_candies(n :: integer, limit :: integer) :: integer
  def distribute_candies(n, limit) do
    Enum.reduce(0..min(n, limit), 0, fn i, ans ->
      ans + helper(n - i, limit)
    end)
  end

  @spec helper(n :: integer, limit :: integer) :: integer
  def helper(n, limit) do
    min_v = max(0, n-limit)
    max_v = min(n, limit)
    max(0, max_v - min_v + 1)
  end

@spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    n = Enum.at(flds, 0) |> String.to_integer()
    limit = Enum.at(flds, 1) |> String.to_integer()
    "n = " <> Integer.to_string(n) <> ", limit = " <> Integer.to_string(limit) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.distribute_candies(n, limit)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
