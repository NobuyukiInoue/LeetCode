defmodule Solution do
  # 307ms - 341ms
  @spec are_similar(mat :: [[integer]], k :: integer) :: boolean
  def are_similar(mat, k) do
    n = Enum.at(mat, 0) |> Enum.count()
    Enum.reduce_while(mat, true, fn row, _ ->
      res =
        Enum.reduce_while(0..n-1, row, fn i, _ ->
          if Enum.at(row, i) != Enum.at(row, rem(i + k, n)) do
            {:halt, false}
          else
            {:cont, true}
          end
        end)
      if not res do
        {:halt, res}
      else
        {:cont, res}
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[[", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "]],[")

    mat =
    for fld <- String.split(Enum.at(flds, 0), "],[") do
      for n <- String.split(fld, ",") do
        String.to_integer(n)
      end
    end

    k = Enum.at(flds, 1) |> String.replace("]]", "") |> String.to_integer()
    "mat = [" <> Mylib.intIntList_to_string(mat) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.are_similar(mat, k)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
