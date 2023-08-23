defmodule Solution do
  # 264ms - 287ms
  @spec arrange_words(text :: String.t) :: String.t
  def arrange_words(text) do
    text
    |> String.split(" ")
    |> Enum.sort_by(&String.length/1)
    |> Enum.join(" ")
    |> String.capitalize()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    text = String.replace(temp, ", ", ",")
    "text = \"" <> text <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.arrange_words(text)
      "result = \"" <> result <> "\""|> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
