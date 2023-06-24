defmodule Solution do
  # 1279ms - 1401ms
  @spec find_non_min_or_max(nums :: [integer]) :: integer
  def find_non_min_or_max(nums) do
    if Enum.count(nums) < 3 do
      -1
    else
      {mi, ma} = Enum.min_max(nums)
      Enum.reduce_while(nums, 0, fn num, _ ->
        if num != mi and num != ma do
          {:halt, num}
        else
          {:cont, num}
        end
      end)
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
      result = Solution.find_non_min_or_max(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
