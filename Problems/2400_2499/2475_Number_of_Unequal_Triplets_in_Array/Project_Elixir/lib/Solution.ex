defmodule Solution do
  # 318ms - 401ms
  @spec unequal_triplets(nums :: [integer]) :: integer
  def unequal_triplets(nums) do
    trip = 0
    pairs = 0
    cnts = for _ <- 0..1001 do 0 end
    unequal_triplets(nums, cnts, 0, trip, pairs)
  end

  @spec unequal_triplets(nums :: [integer], cnts :: [integer], index :: integer, trip :: integer, pairs :: integer) :: integer
  def unequal_triplets(nums, cnts, index, trip, pairs) do
    if nums != [] do
      num = nums |> hd
      cnt = Enum.at(cnts, num)
      trip = trip + pairs - cnt * (index - cnt)
      pairs = pairs + index - cnt
      cnts = List.replace_at(cnts, num, cnt + 1)
      unequal_triplets(nums |> tl, cnts, index + 1, trip, pairs)
    else
      trip
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
      result = Solution.unequal_triplets(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
