defmodule Solution do
  # 302ms - 329ms
  @spec xor_all_nums(nums1 :: [integer], nums2 :: [integer]) :: integer
  def xor_all_nums(nums1, nums2) do
    x = Enum.reduce(nums1, 0, fn num1, x -> Bitwise.bxor(x, num1) end)
    y = Enum.reduce(nums2, 0, fn num2, y -> Bitwise.bxor(y, num2) end)
    Bitwise.bxor(rem(Enum.count(nums1), 2)*y, rem(Enum.count(nums2), 2)*x)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums1 =
      for n <- String.split(Enum.at(flds, 0), ",") do
        String.to_integer(n)
      end

    nums2 =
      for n <- String.split(Enum.at(flds, 1), ",") do
        String.to_integer(n)
      end

    "nums1 = [" <> Mylib.intList_to_string(nums1) <> "], nums2 = [" <> Mylib.intList_to_string(nums2) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.xor_all_nums(nums1, nums2)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
