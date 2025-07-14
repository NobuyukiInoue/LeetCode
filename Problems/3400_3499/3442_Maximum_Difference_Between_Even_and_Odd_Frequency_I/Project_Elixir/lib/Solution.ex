defmodule Solution do
  # 6ms - 7ms
  @spec max_difference(s :: String.t) :: integer
  def max_difference(s) do
    cnts = Enum.reduce(s |> String.to_charlist, %{}, fn ch, cnts ->
      Map.put(cnts, ch, Map.get(cnts, ch, 0) + 1)
    end)
    {max_odd, min_even} =
      Enum.reduce(cnts |> Map.values, {1, s |> String.length}, fn cnt, {max_odd, min_even} ->
        if rem(cnt, 2) == 1 do
          {max(max_odd, cnt), min_even}
        else
          {max_odd, min(min_even, cnt)}
        end
      end)
    max_odd - min_even
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_difference(s)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
