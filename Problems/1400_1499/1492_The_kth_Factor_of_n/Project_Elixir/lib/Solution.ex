defmodule Solution do
  # 262ms - 294ms
  @spec kth_factor(n :: integer, k :: integer) :: integer
  def kth_factor(n, k) do
    {cnt, ans} =
      Enum.reduce_while(1..div(n, 2)+1, {0, 0}, fn i, {cnt, _ans} ->
        if rem(n, i) == 0 do
          if cnt + 1 == k do
            {:halt, {cnt + 1, i}}
          else
            {:cont, {cnt + 1, i}}
          end
        else
          {:cont, {cnt, i}}
        end
      end)
    cond do
      cnt == k -> ans
      cnt == k - 1 -> n
      true -> -1
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")
    n = String.to_integer(Enum.at(flds, 0))
    k = String.to_integer(Enum.at(flds, 1))
    "n = " <> Integer.to_string(n) <> ", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.kth_factor(n, k)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
