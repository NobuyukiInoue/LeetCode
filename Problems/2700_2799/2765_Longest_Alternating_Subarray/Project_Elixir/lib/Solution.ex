defmodule Solution do
  # 627ms - 662ms
  @spec alternating_subarray(nums :: [integer]) :: integer
  def alternating_subarray(nums) do
    n = Enum.count(nums)
    res = Enum.reduce(0..n - 1, 0, fn i, res ->
      Enum.reduce_while(i + 1..n - 1, res, fn j, res ->
        if Enum.at(nums, j) != Enum.at(nums, i) + rem(j - i, 2) do
          {:halt, res}
        else
          {:cont, max(res, j - i + 1)}
        end
      end)
    end)
    if res > 1 do
      res
    else
      -1
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.alternating_subarray(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
