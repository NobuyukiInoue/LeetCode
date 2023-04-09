defmodule Solution do
  # 224ms - 248ms
  @spec smallest_number(pattern :: String.t) :: String.t
  def smallest_number(pattern) do
    smallest_number(pattern, 0, String.length(pattern), "", "")
  end

  @spec smallest_number(pattern :: String.t, idx :: integer, len_patter :: integer, stack :: String.t, res :: String.t) :: String.t
  def smallest_number(_, idx, len_pattern, stack, res) when idx == len_pattern + 1 do
      res <> String.reverse(stack)
  end

  def smallest_number(pattern, idx, _, stack, res) do
    n_stack = stack <> Integer.to_string(idx + 1)
    if String.at(pattern, idx) == "I" do
      smallest_number(pattern, idx + 1, String.length(pattern), "", res <> String.reverse(n_stack))
    else
      smallest_number(pattern, idx + 1, String.length(pattern), n_stack, res)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    pattern = String.replace(temp, ", ", ",")
    "pattern = " <> pattern |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.smallest_number(pattern)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
