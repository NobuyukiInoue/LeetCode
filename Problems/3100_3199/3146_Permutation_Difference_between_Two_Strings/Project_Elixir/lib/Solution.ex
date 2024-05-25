defmodule Solution do
  # 353ms - 360ms
  @spec find_permutation_difference(s :: String.t, t :: String.t) :: integer
  def find_permutation_difference(s, t) do
    Enum.reduce(String.to_charlist(s), 0, fn ch, res ->
      {pos_s, _} = :binary.match(s, <<ch>>)
      {pos_t, _} = :binary.match(t, <<ch>>)
      res + abs(pos_s - pos_t)
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, ", ", ",")
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.split(temp, ",")

    [s | t] = [(flds |> hd) | (flds |> tl |> hd)]
    "s = \"" <> s <> "\", t = \"" <> t <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_permutation_difference(s, t)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
