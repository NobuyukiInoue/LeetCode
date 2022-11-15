use Bitwise

defmodule Solution do
  # 420ms - 539ms
  @spec partition_string(s :: String.t) :: integer
  def partition_string(s) do
    partition_string(String.to_charlist(s), 0, 1)
  end

  @spec partition_string(arr :: [char], map :: integer, count :: integer) :: integer
  def partition_string(arr, map, count) do
    if arr != [] do
      sh = (1 <<< (Enum.at(arr, 0) - 96))
      if (map &&& sh) != 0 do
        partition_string(arr |> tl, bxor(0, sh), count + 1)
      else
        partition_string(arr |> tl, bxor(map, sh), count)
      end
    else
      count
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = " <> s |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.partition_string(s)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
