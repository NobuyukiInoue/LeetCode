defmodule Solution do
  # 531ms - 544ms
  @spec count_bad_pairs(nums :: [integer]) :: integer
  def count_bad_pairs(nums) do
    Enum.reduce(nums, {0, 0, %{}}, fn num, {i, ans, cnt_dict} ->
      prev = Map.get(cnt_dict, i - num, 0)
      {i + 1, ans + (i - prev), Map.put(cnt_dict, i - num, prev + 1)}
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_bad_pairs(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
