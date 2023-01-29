defmodule Solution do
  # 359ms - 410ms
  @spec get_common(nums1 :: [integer], nums2 :: [integer]) :: integer
  def get_common([], _) do
    -1
  end

  def get_common(_, []) do
    -1
  end

  def get_common([head1 | tail1], [head2 | tail2]) when head1 > head2 do
    get_common([head1 | tail1], tail2)
  end

  def get_common([head1 | tail1], [head2 | tail2]) when head1 < head2 do
    get_common(tail1, [head2 | tail2])
  end

  def get_common([head | _], _) do
    head
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums1 = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    nums2 = for num <- String.split(Enum.at(flds, 1), ","), do: num |> String.trim() |> String.to_integer()
    "nums1 = [" <>  Mylib.intList_to_string(nums1) <> "]" |> IO.puts()
    "nums2 = [" <>  Mylib.intList_to_string(nums2) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.get_common(nums1, nums2)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
