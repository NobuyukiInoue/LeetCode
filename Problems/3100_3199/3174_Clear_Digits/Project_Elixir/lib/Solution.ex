defmodule Solution do
  # 310ms - 370ms
  @spec clear_digits(s :: String.t) :: String.t
  def clear_digits(s) do
    s |> String.to_charlist()
      |> Enum.reduce([], fn ch, ans ->
        if ?0 <= ch and ch <= ?9 do
          ans |> tl
        else
          [<<ch>> | ans]
        end
      end)
      |> Enum.reverse()
      |> Enum.join()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.clear_digits(s)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
