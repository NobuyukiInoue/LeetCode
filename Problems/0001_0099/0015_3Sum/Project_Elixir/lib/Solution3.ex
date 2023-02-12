defmodule Solution3 do
  # Time Limit Exceeded
  @spec three_sum(nums :: [integer]) :: [[integer]]
  def three_sum(nums) do
    three_sum(Enum.sort(nums), [], 0, Enum.count(nums) - 2)
  end

  @spec three_sum(nums :: [integer], res :: [[integer]], idx :: integer, max :: integer) :: [[integer]]
  def three_sum(_, res, idx, max) when idx >= max do
#     "idx = " <> Integer.to_string(idx) |> IO.puts()
#     "res = " <> Mylib.intIntList_to_string(res) |> IO.puts()
    res
  end

  def three_sum(nums, res, idx, max) do
#    "idx = " <> Integer.to_string(idx) |> IO.puts()
#    "res = " <> Mylib.intIntList_to_string(res) |> IO.puts()
    if idx > 0 and Enum.at(nums, idx) == Enum.at(nums, idx - 1) do
      three_sum(nums, res, idx + 1, max)
    else
      three_sum(nums, check_res(nums, res, idx, idx + 1, Enum.count(nums) - 1), idx + 1, max)
    end
  end

  @spec check_res(nums :: [integer], res :: [[integer]], idx :: integer, l :: integer, r :: integer) :: [[integer]]
  def check_res(_, res, _, l, r) when l >= r do
#    "l = " <> Integer.to_string(l) <> ", r = " <> Integer.to_string(r) |> IO.puts()
#    "return res." |> IO.puts()
    res
  end

  def check_res(nums, res, idx, l, r) do
#    "check_res() ... nums = [" <> Mylib.intList_to_string(nums) <> "], res = " <> Mylib.intIntList_to_string(res) <> ", l = " <> Integer.to_string(l) <> ", r = " <> Integer.to_string(r) |> IO.puts()
#    "nums[i] = " <> Integer.to_string(Enum.at(nums, idx)) <> ", nums[l] = " <> Integer.to_string(Enum.at(nums, l)) <> ", nums(r) = " <> Integer.to_string(Enum.at(nums, r)) |> IO.puts()
    s = Enum.at(nums, idx) + Enum.at(nums, l) + Enum.at(nums, r)
#    "s = " <> Integer.to_string(s) |> IO.puts()
    cond do
      s > 0 ->
        check_res(nums, res, idx, l, r - 1)
      s < 0 ->
        check_res(nums, res, idx, l + 1, r)
      true ->
        res2 = res ++ [[Enum.at(nums, idx), Enum.at(nums, l), Enum.at(nums, r)]]
#        "res2 = " <> Mylib.intIntList_to_string(res2) |> IO.puts()
        check_res(nums, res2, idx, calc_l(nums, l, r) + 1, calc_r(nums, l, r) - 1)
    end
  end

  @spec calc_l(nums :: [integer], l :: integer, r :: integer) :: integer
  def calc_l(_, l, r) when l >= r do
#    "calc_l() ... nums = [" <> Mylib.intList_to_string(nums) <> "], l = " <> Integer.to_string(l) <> ", r = " <> Integer.to_string(r) |> IO.puts()
    l
  end

  def calc_l(nums, l, r) do
#    "calc_l() ... nums = [" <> Mylib.intList_to_string(nums) <> "], l = " <> Integer.to_string(l) <> ", r = " <> Integer.to_string(r) |> IO.puts()
    if Enum.at(nums, l) == Enum.at(nums, l + 1) do
      calc_l(nums, l + 1, r)
    else
      l
    end
  end

  @spec calc_r(nums :: [integer], l :: integer, r :: integer) :: integer
  def calc_r(_, l, r) when l >= r do
#    "calc_r() ... nums = [" <> Mylib.intList_to_string(nums) <> "], l = " <> Integer.to_string(l) <> ", r = " <> Integer.to_string(r) |> IO.puts()
    r
  end

  def calc_r(nums, l, r) do
#    "calc_r() ... nums = [" <> Mylib.intList_to_string(nums) <> "], l = " <> Integer.to_string(l) <> ", r = " <> Integer.to_string(r) |> IO.puts()
    if Enum.at(nums, r) == Enum.at(nums, r - 1) do
      calc_r(nums, l, r - 1)
    else
      r
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, ",")

    nums = for n <- flds, do: n |> String.trim() |> String.to_integer()
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.three_sum(nums)
      "result = " <> Mylib.intIntList_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
    :ok
  end
end
