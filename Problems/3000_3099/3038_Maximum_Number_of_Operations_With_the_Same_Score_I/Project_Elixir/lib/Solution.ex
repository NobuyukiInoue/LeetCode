defmodule Solution do
  # 264ms - 302ms
  @spec max_operations(nums :: [integer]) :: integer
  def max_operations(nums) do
    [h0 | [h1 | _]] = nums
    helper(nums, h0 + h1, 0)
  end

  @spec helper(nums :: [integer], total :: integer, ans :: integer) :: integer
  def helper([_h0 | []], _total, ans) do
    ans
  end

  def helper([h0 | [h1 | []]], total, ans) when h0 + h1 != total do
    ans
  end

  def helper([_h0 | [_h1 | []]], _total, ans) do
    ans + 1
  end

  def helper([h0 | [h1 | _tail]], total, ans) when h0 + h1 != total do
    ans
  end

  def helper([_h0 | [_h1 | tail]], total, ans)  do
    helper(tail, total, ans + 1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_operations(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
