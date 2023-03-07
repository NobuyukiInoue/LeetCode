defmodule Solution do
  # 237ms -  273ms
  @spec left_rigth_difference(nums :: [integer]) :: [integer]
  def left_rigth_difference(nums) do
    left_rigth_difference(nums, 0, Enum.sum(nums), [])
  end

  @spec left_rigth_difference(nums :: [integer], left :: integer, right :: integer, ans :: [integer]) :: [integer]
  def left_rigth_difference([head | tail], left, right, ans) do
    n_left = left + head
    cur = abs(n_left - right)
    n_right = right - head
    left_rigth_difference(tail, n_left, n_right, ans ++ [cur])
  end

  def left_rigth_difference([], _, _, ans) do
    ans
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.left_rigth_difference(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
