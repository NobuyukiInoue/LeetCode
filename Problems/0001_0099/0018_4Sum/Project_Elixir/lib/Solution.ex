defmodule Solution do
  # 372ms - 385ms
  @spec four_sum(nums :: [integer], target :: integer) :: [[integer]]
  def four_sum(nums, target) do
    df(Enum.sort(nums), 0, Enum.count(nums) - 1, target, 4, [], []) |> Enum.reverse()
  end

  @spec df(nums :: [integer], l :: integer, r :: integer, target:: integer, limit_n :: integer, ans :: [[integer]], res :: [integer]) :: [[integer]]
  def df(nums, l, r, target, limit_n, ans, res) do
    cond do
    r - l + 1 < limit_n or limit_n < 2 or target < Enum.at(nums, l)*limit_n or target > Enum.at(nums, r)*limit_n ->
      ans
    limit_n == 2 ->
      loop_lr(nums, l, r, target, ans, res)
    true ->
      if r > l do
#       bad.
#       Enum.map(idx, fn(i) ->
#         if i == l or (i > l and Enum.at(nums, i - 1) != Enum.at(nums, i)) do
#           df(nums, i + 1, r, target - Enum.at(nums, i), limit_n - 1, ans, [Enum.at(nums, i) | res])
#         end
#       end)
        idx = for i <- l..r do i end
        loop_df(nums, idx, l, r, target, limit_n, ans, res)
      else
        ans
      end
    end
  end

  @spec loop_df(nums :: [integer], idx :: [integer], l :: integer, r :: integer, target:: integer, limit_n :: integer, ans :: [[integer]], res :: [integer]) :: [[integer]]
  def loop_df(nums, [head | tail], l, r, target, limit_n, ans, res) do
    if head == l or (head > l and Enum.at(nums, head - 1) != Enum.at(nums, head)) do
      n_ans = df(nums, head + 1, r, target - Enum.at(nums, head), limit_n - 1, ans, [Enum.at(nums, head) | res])
      loop_df(nums, tail, l, r, target, limit_n, n_ans, res)
    else
      loop_df(nums, tail, l, r, target, limit_n, ans, res)
    end
  end

  def loop_df(_, [], _, _, _, _, ans, _) do
    ans
  end

  @spec loop_lr(nums :: [integer], l :: integer, r :: integer, target :: integer, ans :: [[integer]], res :: [integer]) :: [[integer]]
  def loop_lr(nums, l, r, target, ans, res) when l < r do
    s = Enum.at(nums, l) + Enum.at(nums, r)
    if s == target do
      loop_lr(nums, calc_l(nums, l + 1, r), r, target, [[Enum.at(nums, l) | [Enum.at(nums, r) | res]] |> Enum.reverse() | ans], res)
    else
      if s < target do
        loop_lr(nums, l + 1, r, target, ans, res)
      else
        loop_lr(nums, l, r - 1, target, ans, res)
      end
    end
  end

  def loop_lr(_, _, _, _, ans, _) do
    ans
  end

  @spec calc_l(nums :: integer, l :: integer, r :: integer) :: integer
  def calc_l(nums, l, r) when l < r do
    if Enum.at(nums, l - 1) == Enum.at(nums, l) do
      calc_l(nums, l + 1, r)
    else
      l
    end
  end

  def calc_l(_, l, _) do
    l
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums =
      for n <- String.split(Enum.at(flds, 0), ",") do
        String.to_integer(n)
      end
    target = String.to_integer(Enum.at(flds, 1))

    "nums = [" <> Mylib.intList_to_string(nums) <> "], target = " <> Integer.to_string(target) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.four_sum(nums, target)
      "result = [" <> Mylib.intIntList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
