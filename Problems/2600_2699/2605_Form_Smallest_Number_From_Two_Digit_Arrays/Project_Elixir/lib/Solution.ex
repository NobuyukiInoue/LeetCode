defmodule Solution do
  # 292ms - 295ms
  @spec min_number(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_number(nums1, nums2) do
    n1 = Enum.sort(nums1)
    n2 = Enum.sort(nums2)
    min_number(n1, n2, Enum.at(n1, 0))
  end

  @spec min_number(nums1 :: [integer], nums2 :: [integer], d1 :: integer) :: integer
  def min_number([head | tail], nums2, d1) do
    if Enum.member?(nums2, head) do
      head
    else
      min_number(tail, nums2, d1)
    end
  end

  def min_number([], nums2, d1) do
    d2 = nums2 |> hd
    if d1 < d2 do
      10*d1 + d2
    else
      10*d2 + d1
    end
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
      result = Solution.min_number(nums1, nums2)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
