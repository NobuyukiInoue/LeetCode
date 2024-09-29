defmodule Solution do
  # 28ms - 32ms
  @spec diagonal_sort(mat :: [[integer]]) :: [[integer]]
  def diagonal_sort(mat) do
    {m, n} = {Enum.count(mat), Enum.count(mat |> hd)}
    mat =
      if n - 2 > 0 do
        Enum.reduce(0..n-2, mat, fn c, mat ->
          d = Enum.sort(for i <- 0..min(n - c, m)-1 do; Enum.at(Enum.at(mat, i), c + i) end)
          if Enum.count(d) - 1 > 0 do
            Enum.reduce(0..Enum.count(d)-1, mat, fn i, mat ->
              List.replace_at(mat, i, List.replace_at(Enum.at(mat, i), c + i, Enum.at(d, i)))
            end)
          else
            mat
          end
        end)
      else
        mat
      end
    if m - 2 > 0 do
      Enum.reduce(0..m-2, mat, fn r, mat ->
        d = Enum.sort(for i <- 0..min(n, m - r)-1 do; Enum.at(Enum.at(mat, r + i), i) end)
        if Enum.count(d) - 1 > 0 do
            Enum.reduce(0..Enum.count(d)-1, mat, fn i, mat ->
            List.replace_at(mat, r + i, List.replace_at(Enum.at(mat, r + i), i, Enum.at(d, i)))
          end)
        else
          mat
        end
      end)
    else
      mat
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    flds = String.split(temp, "],[")

    mat =
    for row <- flds do
      for col <- String.split(row, ",") do
        String.to_integer(col)
      end
    end

    "mat = [" <> Mylib.intIntList_to_string(mat) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.diagonal_sort(mat)
      "result = [" <> Mylib.intIntList_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
