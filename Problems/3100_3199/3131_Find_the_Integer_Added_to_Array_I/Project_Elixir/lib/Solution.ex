defmodule Solution do
  # 314ms - 379ms
  @spec added_integer(nums1 :: [integer], nums2 :: [integer]) :: integer
  def added_integer(nums1, nums2) do
    Enum.min(nums2) - Enum.min(nums1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums1 =
      for num <- String.split(Enum.at(flds, 0), ",") do
          String.to_integer(num)
      end
    nums2 =
      for num <- String.split(Enum.at(flds, 1), ",") do
          String.to_integer(num)
      end

    "nums1 = " <> Mylib.intList_to_string(nums1) <> ", nums2 = " <> Mylib.intList_to_string(nums2) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.added_integer(nums1, nums2)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
