defmodule Solution do
  # 358ms - 395ms
  @spec repeated_character(s :: String.t) :: char
  def repeated_character(s) do
    s |> String.to_charlist() |> is_member(MapSet.new())
  end

  def is_member([c | cs], set) do
    if MapSet.member?(set, c) do
      c
    else
      is_member(cs, MapSet.put(set, c))
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    s = String.replace(temp, "\"", "")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.repeated_character(s)
      "result = \"" <> to_string(result) <> "\""|> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
