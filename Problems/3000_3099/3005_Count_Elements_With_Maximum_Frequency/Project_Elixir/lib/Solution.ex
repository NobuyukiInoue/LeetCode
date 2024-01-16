defmodule Solution do
  # 295ms - 312ms
  @spec max_frequency_elements(nums :: [integer]) :: integer
  def max_frequency_elements(nums) do
    cnts = Enum.reduce(nums, %{}, fn num, cnts -> Map.update(cnts, num, 1, &(&1 + 1)) end)
    lst = Map.values(cnts)
    max_cnts = Enum.max(lst)
    Enum.filter(lst, fn val -> val == max_cnts end) |> Enum.sum()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_frequency_elements(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
