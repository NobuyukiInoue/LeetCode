defmodule Solution do
  # 334ms - 342ms
  @spec duplicate_numbers_xor(nums :: [integer]) :: integer
  def duplicate_numbers_xor(nums) do
    cnts =
      Enum.reduce(nums, %{}, fn num, cnts ->
        Map.put(cnts, num, Map.get(cnts, num, 0) + 1)
      end)
    twices = Map.filter(cnts, fn {_k, v} -> v == 2 end)
    Enum.reduce(Map.keys(twices), 0, fn k, ans->
      Bitwise.bxor(ans, k)
    end)
  end

  # 375ms - 377ms
  @spec duplicate_numbers_xor2(nums :: [integer]) :: integer
  def duplicate_numbers_xor2(nums) do
    nums
    |>
      Enum.reduce(%{}, fn num, cnts ->
        Map.put(cnts, num, Map.get(cnts, num, 0) + 1)
      end)
    |> Map.filter(fn {_k, v} -> v == 2 end)
    |> Map.keys()
    |> Enum.reduce(0, fn k, ans-> Bitwise.bxor(ans, k) end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.duplicate_numbers_xor(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
