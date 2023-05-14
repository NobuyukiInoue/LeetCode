defmodule Solution do
  # 251ms - 253ms
  @spec remove_occurrences(s :: String.t, part :: String.t) :: String.t
  def remove_occurrences(s, part) do
    if String.contains?(s, part) do
      remove_occurrences(String.replace(s, part, "", global: false), part)
    else
      s
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    s = Enum.at(flds, 0)
    part = Enum.at(flds, 1)
    "s = \"" <> s <> "\", part = \"" <> part <> "\"" |> IO.puts()

    execright = Benchmark.measure(fn ->
      result = Solution.remove_occurrences(s, part)
      "result = \"" <> result <> "\"" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(execright, 3)) <> " [s]\n" |> IO.puts()
  end
end
