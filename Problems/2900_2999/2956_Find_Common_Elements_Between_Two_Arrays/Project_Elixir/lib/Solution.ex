defmodule Solution do
  # 382ms - 398ms
  @spec find_intersection_values(nums1 :: [integer], nums2 :: [integer]) :: [integer]
  def find_intersection_values(nums1, nums2) do
    res1 = Enum.reduce(nums1, 0, fn num, res -> if num in nums2 do; res + 1 else res end end)
    res2 = Enum.reduce(nums2, 0, fn num, res -> if num in nums1 do; res + 1 else res end end)
    [res1, res2]
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums1 = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    nums2 = for num <- String.split(Enum.at(flds, 1), ","), do: num |> String.trim() |> String.to_integer()
    "nums1 = [" <>  Mylib.intList_to_string(nums1) <> "], nums2 = [" <>  Mylib.intList_to_string(nums1) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_intersection_values(nums1, nums2)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
