defmodule Solution do
  # 266ms - 299ms
  @spec count_pairs(nums :: [integer], target :: integer) :: integer
  def count_pairs(nums, target) do
    nums = Enum.sort(nums)
    n = Enum.count(nums)
    Enum.reduce(0..n-2, 0, fn i, ans ->
      nums_i = Enum.at(nums, i)
      Enum.reduce_while(i+1..n-1, ans, fn j, ans ->
        if nums_i + Enum.at(nums, j) >= target do
          {:halt, ans}
        else
          {:cont, ans + 1}
        end
      end)
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    target = Enum.at(flds, 1) |> String.to_integer()
    "nums = [" <>  Mylib.intList_to_string(nums) <> "], target = " <> Integer.to_string(target) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_pairs(nums, target)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
