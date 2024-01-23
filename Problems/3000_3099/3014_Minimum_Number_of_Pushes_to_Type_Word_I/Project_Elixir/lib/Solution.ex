defmodule Solution do
  # 284ms - 356ms
  @spec minimum_pushes(word :: String.t) :: integer
  def minimum_pushes(word) do
    n = String.length(word)
    quotient = div(n, 8)
    cond do
      quotient == 0 -> rem(n, 8)
      quotient == 1 -> 8 + rem(n, 8)*2
      true ->
        {row, ans} = Enum.reduce(quotient..1, {1, 0}, fn _, {row, ans} ->
          {row + 1, ans + row*8}
        end)
        ans + rem(n, 8)*row
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    word = String.replace(temp, ", ", ",")
    "word = \"" <> word <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_pushes(word)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
