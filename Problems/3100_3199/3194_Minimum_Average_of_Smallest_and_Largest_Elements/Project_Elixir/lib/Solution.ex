defmodule Solution do
  # 301ms - 314ms
  @spec minimum_average(nums :: [integer]) :: float
  def minimum_average(nums) do
    n = Enum.count(nums)
    s_nums = Enum.sort(nums)
    ans = ((s_nums |> hd) + Enum.at(s_nums, n - 1))/2.0
    Enum.reduce(1..div(n,2), ans, fn i, ans ->
      min(ans, (Enum.at(s_nums, i) + Enum.at(s_nums, n - i - 1))/2.0)
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_average(nums)
      "result = " <> Float.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
