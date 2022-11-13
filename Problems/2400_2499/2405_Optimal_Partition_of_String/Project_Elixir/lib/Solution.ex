defmodule Solution do
  # 350ms - 370ms
  @spec distinct_averages(nums :: [integer]) :: integer
  def distinct_averages(nums) do
    nums = Enum.sort(nums)
    n = Enum.count(nums)
    lst = (for i <- 0..div(n, 2)-1 do
      (Enum.at(nums, i) + Enum.at(nums, n - i - 1))/ 2.0
    end)
    aves = Enum.reduce lst, %{}, fn x, acc ->
      Map.put(acc, x, 1)
    end
    map_size(aves)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.distinct_averages(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
