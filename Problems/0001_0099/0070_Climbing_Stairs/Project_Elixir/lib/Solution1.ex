defmodule Solution1 do
  # 283ms - 324ms
  @spec climb_stairs(n :: integer) :: integer
  def climb_stairs(n) do
    res = for _ <- 0..n+1, do: 0

    res =
    if n > 0 do
      res = List.replace_at(res, 1, 1)
      if n > 1 do
        List.replace_at(res, 2, 2)
      else
        res
      end
    else
      res
    end
    "res = [" <> Mylib.intList_to_string(res) <> "]" |> IO.puts()

    res =
    if n >= 3 do
      Enum.reduce(3..n, res, fn i, res ->
        List.replace_at(res, i, Enum.at(res, i - 1) + Enum.at(res, i - 2))
      end)
    else
      res
    end

    "res = [" <> Mylib.intList_to_string(res) <> "]" |> IO.puts()
    Enum.at(res, n)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    n = temp |> String.to_integer()
    "n = " <>  Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.climb_stairs(n)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
