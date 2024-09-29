defmodule Solution do
  # 0ms
  @spec min_element(nums :: [integer]) :: integer
  def min_element(nums) do
    Enum.reduce(nums, get_digit_sum(nums |> hd, 0), fn num, ans ->
      min(ans, get_digit_sum(num, 0))
    end)
  end

  @spec get_digit_sum(num :: integer, sum :: integer) :: integer
  def get_digit_sum(num, sum) when num == 0 do
    sum
  end

  def get_digit_sum(num, sum) do
    get_digit_sum(div(num, 10), sum + rem(num, 10))
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.min_element(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
