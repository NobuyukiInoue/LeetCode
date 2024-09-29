defmodule Solution do
  # 0ms
  @spec kth_character(k :: integer) :: char
  def kth_character(k) do
    ?a + (for(<<bit::1 <- :binary.encode_unsigned(k - 1)>>, do: bit) |> Enum.sum)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    k = String.to_integer(flds)
    "k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.kth_character(k)
      "result = " <> <<result>> |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
