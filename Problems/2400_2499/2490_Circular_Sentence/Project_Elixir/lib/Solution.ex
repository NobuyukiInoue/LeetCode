use Bitwise

defmodule Solution do
  # 378ms - 404ms
  @spec is_circular_sentence(sentence :: String.t) :: boolean
  def is_circular_sentence(sentence) do
    lst =
      sentence
      |> String.split(" ")
      |> Enum.map(fn s ->
        lst = s |> String.graphemes()
        [List.first(lst), List.last(lst)]
      end)
    (lst ++ [hd(lst)])
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.all?(fn [[_, t], [f, _]] -> t == f end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    sentence = String.replace(temp, ", ", ",")
    "sentence = " <> sentence |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_circular_sentence(sentence)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
