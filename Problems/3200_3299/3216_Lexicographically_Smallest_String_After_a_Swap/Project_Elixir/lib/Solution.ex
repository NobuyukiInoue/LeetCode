defmodule Solution do
  # 332ms - 377ms
  @spec get_smallest_string(s :: String.t) :: String.t
  def get_smallest_string(s) do
    n = String.length(s)
    Enum.reduce_while(0..n-2, s, fn i, s ->
      {c1, c2} = {String.at(s, i), String.at(s, i + 1)}
      {m1, m2} = {rem(String.to_integer(c1), 2), rem(String.to_integer(c2), 2)}
      if m1 == m2 and c1 > c2 do
        if i == 0 do
          {:halt, c2 <> c1 <> String.slice(s, i+2..n-1)}
        else
          {:halt, String.slice(s, 0..i-1) <> c2 <> c1 <> String.slice(s, i+2..n-1)}
        end
      else
        {:cont, s}
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.get_smallest_string(s)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
