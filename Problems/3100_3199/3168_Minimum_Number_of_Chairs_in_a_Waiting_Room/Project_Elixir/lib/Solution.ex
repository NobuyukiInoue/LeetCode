defmodule Solution do
  # 313ms - 349ms
  @spec minimum_chairs(s :: String.t) :: integer
  def minimum_chairs(s) do
    s |> String.to_charlist()
      |> Enum.reduce({0, 0}, fn ch, {ans, cnt} ->
        cnt = if ch == ?E do; cnt + 1 else; cnt - 1 end
        {max(ans, cnt), cnt}
      end)
      |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_chairs(s)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
