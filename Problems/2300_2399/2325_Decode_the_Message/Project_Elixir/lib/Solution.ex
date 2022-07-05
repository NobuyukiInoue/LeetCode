defmodule Solution do
  @spec decode_message(key :: String.t, message :: String.t) :: String.t
  # 282ms - 343ms
  def decode_message(key, message) do
    key
    |> String.replace(" ", "")
    |> String.to_charlist()
    |> Enum.reduce({%{}, 0}, fn k, {acc, i} ->
      if Map.has_key?(acc, k) do
        {acc, i}
      else
        {Map.put(acc, k, ?a + i), i + 1}
      end
    end)
#   |> then(fn {dt, _} ->
    |> (fn {dt, _} ->
      message
      |> String.to_charlist()
      |> Enum.map(&(dt[&1] || &1))
      |> List.to_string()
    end).()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, ",")
    key = Enum.at(flds, 0)
    message = Enum.at(flds, 1)

    "key = \"" <> key <> "\"" |> IO.puts()
    "message = \"" <> message <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.decode_message(key, message)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
