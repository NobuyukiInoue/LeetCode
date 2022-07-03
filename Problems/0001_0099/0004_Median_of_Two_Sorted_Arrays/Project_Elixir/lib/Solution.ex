defmodule Solution do
  @spec find_median_sorted_arrays(nums1 :: [integer], nums2 :: [integer]) :: float
  def find_median_sorted_arrays(nums1, nums2) do
    # 496ms - 721ms
    arr = Enum.sort(nums1 ++ nums2)
    count = Enum.count(arr)
    mid = div(count, 2)
    if (rem(count, 2) == 0) do
      (Enum.at(arr, mid - 1) + Enum.at(arr, mid)) / 2
    else
      (Enum.at(arr, mid))/1
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums1 = for n <- String.split(Enum.at(flds, 0), ","), do: n |> String.trim() |> String.to_integer()
    nums2 = for n <- String.split(Enum.at(flds, 1), ","), do: n |> String.trim() |> String.to_integer()
    "nums1 = [" <> Mylibs.intListToString(nums1) <> "]" |> IO.puts()
    "nums2 = [" <> Mylibs.intListToString(nums2) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_median_sorted_arrays(nums1, nums2)
      "result = " <> Float.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
