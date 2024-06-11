defmodule Solution do
  # 353ms - 354ms
  @spec number_of_pairs(nums1 :: [integer], nums2 :: [integer], k :: integer) :: integer
  def number_of_pairs(nums1, nums2, k) do
    Enum.reduce(nums1, 0, fn num1, ans ->
      Enum.reduce(nums2, ans, fn num2, ans ->
        if rem(num1, num2*k) == 0 do
          ans + 1
        else
          ans
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

    nums1 =
      for num <- String.split(Enum.at(flds, 0), ",") do
          String.to_integer(num)
      end
    nums2 =
      for num <- String.split(Enum.at(flds, 1), ",") do
          String.to_integer(num)
      end
    k = String.to_integer(Enum.at(flds, 2))

    "nums1 = [" <> Mylib.intList_to_string(nums1) <> "], nums2 = [" <> Mylib.intList_to_string(nums2) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.number_of_pairs(nums1, nums2, k)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
