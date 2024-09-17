defmodule Solution do
  # 5ms - 8ms
  @spec convert_date_to_binary(date :: String.t) :: String.t
  def convert_date_to_binary(date) do
    String.split(date, "-")
    |> Enum.reduce([], fn fld, ans ->
        [Integer.to_charlist(String.to_integer(fld), 2)] ++ ans
      end)
    |> Enum.reverse()
    |> Enum.join("-")
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    date = String.replace(temp, ", ", ",")
    "s = \"" <> date <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.convert_date_to_binary(date)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
