defmodule Solution do
  # 1488ms 1490ms
  @spec max_sum_after_partitioning(arr :: [integer], k :: integer) :: integer
  def max_sum_after_partitioning(arr, k) do
    n = Enum.count(arr)
    if n < 2 do
      Enum.sum(arr)
    else
      dp = for _ <- 0..n-1, do: 0
      arr0 = arr |> hd
      dp = List.replace_at(dp, 0, arr0)
      dp =
        if k > 1 do
          Enum.reduce(1..k-1, {arr0, dp}, fn i, {max_val, dp} ->
            max_val = max(max_val, Enum.at(arr, i))
            {max_val, List.replace_at(dp, i, max_val*(i + 1))}
          end) |> elem(1)
        else
          dp
        end
      {_, dp} =
      Enum.reduce(k..n-1, {0, dp}, fn i, {_, dp} ->
        if n > k do
          if k > 1 do
            Enum.reduce(1..k, {Enum.at(arr, i), dp}, fn j, {max_val, dp} ->
              max_val = max(max_val, Enum.at(arr, i - j + 1))
              {max_val, List.replace_at(dp, i, max(Enum.at(dp, i), Enum.at(dp, i - j) + max_val*j))}
            end)
          else
            max_val = Enum.at(arr, i)
            {max_val, List.replace_at(dp, i, max(Enum.at(dp, i), Enum.at(dp, i - 1) + max_val))}
          end
        else
          {0, dp}
        end
      end)

      Enum.at(dp, n - 1)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    arr = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()
    "arr = [" <>  Mylib.intList_to_string(arr) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_sum_after_partitioning(arr, k)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
