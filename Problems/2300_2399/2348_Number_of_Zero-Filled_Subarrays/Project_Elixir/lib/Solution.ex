defmodule Solution do
  # 355ms - 362ms
  @spec zero_filled_subarray(nums :: [integer]) :: integer
  def zero_filled_subarray(nums) do
    zero_filled_subarray(nums, 0, -1, 0)
  end

  @spec zero_filled_subarray(nums :: [integer], i :: integer, j :: integer, ans :: integer) :: integer
  def zero_filled_subarray([head | tail], i, _, ans) when head != 0 do
    zero_filled_subarray(tail, i + 1, i, ans)
  end

  def zero_filled_subarray([_ | tail], i, j, ans) do
    zero_filled_subarray(tail, i + 1, j, ans + (i - j))
  end

  def zero_filled_subarray([], _, _, ans) do
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
      result = Solution.zero_filled_subarray(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
