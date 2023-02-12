defmodule Solution do
  # 343ms - 407ms
  @spec find_the_array_conc_val(nums :: [integer]) :: integer
  def find_the_array_conc_val(nums) do
    find_the_array_conc_val(nums, 0, Enum.count(nums) - 1, 0)
  end

  @spec find_the_array_conc_val(nums :: [integer], i :: integer, j :: integer, ans :: integer) :: integer
  def find_the_array_conc_val(_, i, j, ans) when i > j do
    ans
  end

  def find_the_array_conc_val(nums, i, j, ans) when i < j do
    find_the_array_conc_val(nums, i + 1, j - 1, ans + String.to_integer(Integer.to_string(Enum.at(nums, i)) <> Integer.to_string(Enum.at(nums, j))))
  end

  def find_the_array_conc_val(nums, i, j, ans) when i == j do
    ans + String.to_integer(Integer.to_string(Enum.at(nums, i)))
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_the_array_conc_val(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
