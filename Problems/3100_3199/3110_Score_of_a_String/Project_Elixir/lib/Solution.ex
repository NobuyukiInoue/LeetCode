defmodule Solution do
  # 293ms - 335ms
  @spec score_of_string(s :: String.t) :: integer
  def score_of_string(s) do
    arr_s = String.to_charlist(s)
    Enum.reduce(arr_s |> tl, {0, arr_s |> hd}, fn ch, {ans, prev} ->
      {ans + abs(ch - prev), ch}
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
      result = Solution.score_of_string(s)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
