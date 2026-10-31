defmodule Solution do
  # 1ms
  @spec dominant_indices(nums :: [integer]) :: integer
  def dominant_indices(nums) do
    nums
    |> Enum.reverse()
    |> Enum.reduce({0, 0, 0}, fn num, {total, cnt, ans} ->
      new_ans = if num * cnt > total, do: ans + 1, else: ans
      {total + num, cnt + 1, new_ans}
    end)
    |> elem(2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.dominant_indices(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
