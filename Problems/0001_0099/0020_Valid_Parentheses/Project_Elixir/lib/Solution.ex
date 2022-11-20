defmodule Solution do
  # 282ms - 456ms
  @spec is_valid(s :: String.t) :: boolean
  def is_valid(s) do
    s |> String.split("", trim: true) |> check([])
  end

  def check([], []), do: true
  def check(["(" | s_tail], queue), do: check(s_tail, ["(" | queue])
  def check(["[" | s_tail], queue), do: check(s_tail, ["[" | queue])
  def check(["{" | s_tail], queue), do: check(s_tail, ["{" | queue])
  def check([")" | s_tail], ["(" | q_tail]), do: check(s_tail, q_tail)
  def check(["]" | s_tail], ["[" | q_tail]), do: check(s_tail, q_tail)
  def check(["}" | s_tail], ["{" | q_tail]), do: check(s_tail, q_tail)
  def check(_, _), do: false

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    s = String.replace(temp, "\"", "")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_valid(s)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
