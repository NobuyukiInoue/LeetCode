defmodule Solution do
  # 454ms - 488ms
  @spec row_and_maximum_ones(mat :: [[integer]]) :: [integer]
  def row_and_maximum_ones(mat) do
    row_and_maximum_ones(mat, 0, 0, 0)
  end

  @spec row_and_maximum_ones(mat :: [[integer]], idx :: integer, ans_idx :: integer, max_cnt :: integer) :: [integer]
  def row_and_maximum_ones([head | tail], idx, ans_idx, max_cnt) do
    cnt = row_and_maximum_ones(head, 0)
    if cnt > max_cnt do
      row_and_maximum_ones(tail, idx + 1, idx, cnt)
    else
      row_and_maximum_ones(tail, idx + 1, ans_idx, max_cnt)
    end
  end

  def row_and_maximum_ones([], _, ans_idx, max_cnt) do
    [ans_idx, max_cnt]
  end

  @spec row_and_maximum_ones(row :: [integer], cnt :: integer) :: integer
  def row_and_maximum_ones([head | tail], cnt) when head == 1 do
    row_and_maximum_ones(tail, cnt + 1)
  end

  def row_and_maximum_ones([_ | tail], cnt) do
    row_and_maximum_ones(tail, cnt)
  end

  def row_and_maximum_ones([], cnt) do
    cnt
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    mat =
    for fld <- flds do
      for n <- String.split(fld, ",") do
        String.to_integer(n)
      end
    end

    Mylib.matrix_to_string("mat", mat) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.row_and_maximum_ones(mat)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
