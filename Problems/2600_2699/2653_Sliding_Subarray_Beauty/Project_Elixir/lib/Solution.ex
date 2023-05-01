defmodule Solution do
  # Time Limite Exceeded.
  @spec get_subarray_beauty(nums :: [integer], k :: integer, x :: integer) :: [integer]
  def get_subarray_beauty(nums, k, x) do
    n = Enum.count(nums)
    freq = for _ <- 0..50, do: 0
    ans = for _ <- 0..n - k, do: 0
    {ans, _} = get_subarray_beauty(nums, n, x, k, 0, 0, 0, freq, ans)
    ans
  end

  @spec get_subarray_beauty(nums :: [integer], nums_len :: integer, x :: integer, k :: integer, i :: integer, j :: integer, idx :: integer, freq :: [integer], ans :: [integer]) :: {[integer], [integer]}
  def get_subarray_beauty(nums, nums_len, x, k, i, j, idx, freq, ans) do
#    "14: x" <> Integer.to_string(x) <> ", k = " <> Integer.to_string(k) <> ", i = " <> Integer.to_string(i) <> ", j = " <> Integer.to_string(j) |> IO.puts()
#    "15: idx = " <> Integer.to_string(idx)
#    "16: freq = [" <> Mylib.intList_to_string(freq) <> "]" |> IO.puts()
#    "17: ans = [" <> Mylib.intList_to_string(ans) <> "]" |> IO.puts()
    if i == nums_len do
      {ans, freq}
    else
      freq_idx = abs(Enum.at(nums, i))
      freq =
        if Enum.at(nums, i) < 0 do
          List.replace_at(freq, freq_idx, Enum.at(freq, freq_idx) + 1)
        else
          freq
        end

      if i - j + 1 >= k do
        freq_idx = abs(Enum.at(nums, j))
        {cur_ans, cur_freq} = loop_j(nums, x, j, idx, freq, Enum.at(freq, freq_idx))
#        "32: cur_ans = " <> Integer.to_string(cur_ans) <> ", cur_freq = " <> Integer.to_string(cur_freq) |> IO.puts()
        freq = List.replace_at(freq, freq_idx, cur_freq)
        ans = List.replace_at(ans, idx, cur_ans)
        get_subarray_beauty(nums, nums_len, x, k, i + 1, j + 1, idx + 1, freq, ans)
      else
        get_subarray_beauty(nums, nums_len, x, k, i + 1, j, idx, freq, ans)
      end
    end
  end

  @spec loop_j(nums :: [integer], x :: integer, j :: integer, idx :: integer, freq :: [integer], cur_freq :: integer) :: {integer, integer}
  def loop_j(nums, x, j, idx, freq, cur_freq) do
    {cur_ans, n_cnt} = loop_l(x, 0, idx, freq, 50)
    cur_ans =
      if n_cnt < x do
        0
      else
        cur_ans
      end
    cur_freq =
      if Enum.at(nums, j) < 0 do
        cur_freq - 1
      else
        cur_freq
      end
    {cur_ans, cur_freq}
  end

  @spec loop_l(x :: integer, cnt :: integer, idx :: integer, freq :: [integer], l :: integer) :: {integer, integer}
  def loop_l(x, cnt, idx, freq, l) when l > 0 do
    n_cnt = cnt + Enum.at(freq, l)
    if n_cnt >= x do
      {-l, n_cnt}
    else
      loop_l(x, n_cnt, idx, freq, l - 1)
    end
  end

  def loop_l(_, cnt, _, _, l) when l == 0 do
    {0, cnt}
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()
    x = Enum.at(flds, 2) |> String.to_integer()
    "flds = [" <>  Mylib.intList_to_string(nums) <> "], k = " <> Integer.to_string(k) <> ", x = " <> Integer.to_string(x) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.get_subarray_beauty(nums, k, x)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
