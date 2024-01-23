defmodule Solution do
  # 660ms - 762ms
  @spec matrix_sum(nums :: [[integer]]) :: integer
  def matrix_sum(nums) do
    sorted_nums = Enum.reduce(nums, [], fn row, sorted_nums ->
      [Enum.sort(row, :desc)] ++ sorted_nums
    end)

    cols =
      for row <- Enum.zip(sorted_nums) do
        Tuple.to_list(row)
      end

    Enum.reduce(cols, 0, fn col, ans ->
      ans + Enum.max(col)
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums =
      for row <- flds do
        for col <- String.split(row, ",") do
          String.to_integer(col)
        end
      end

    "nums = [" <> Mylib.intIntList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.matrix_sum(nums)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
