defmodule Solution do
  # 318ms - 340ms
  @spec merge_arrays(nums1 :: [[integer]], nums2 :: [[integer]]) :: [[integer]]
  def merge_arrays(nums1, nums2) do
    merge_arrays(nums1, nums2, 0, 0, [])
  end

  @spec merge_arrays(nums1 :: [[integer]], nums2 :: [[integer]], i :: integer, j :: integer, res :: [[integer]]) :: [[integer]]
  def merge_arrays(nums1, nums2, i, j, res) do
#   if res != [] do
#     "res = " <> Mylib.intIntList_to_string(res) |> IO.puts()
#   else
#     "res = " <> "[]" |> IO.puts()
#   end
    if i < Enum.count(nums1) or j < Enum.count(nums2) do
      cond do
      i == Enum.count(nums1) ->
        merge_arrays(nums1, nums2, i, j + 1, res ++ [Enum.at(nums2, j)])
      j == Enum.count(nums2) ->
        merge_arrays(nums1, nums2, i + 1, j, res ++ [Enum.at(nums1, i)])
      true ->
        cond do
        Enum.at(Enum.at(nums1, i), 0) == Enum.at(Enum.at(nums2, j), 0) ->
          merge_arrays(nums1, nums2, i + 1, j + 1, res ++ [[Enum.at(Enum.at(nums1, i), 0), Enum.at(Enum.at(nums1, i), 1) + Enum.at(Enum.at(nums2, j), 1)]])
        Enum.at(Enum.at(nums1, i), 0) < Enum.at(Enum.at(nums2, j), 0) ->
          merge_arrays(nums1, nums2, i + 1, j, res ++ [Enum.at(nums1, i)])
        true ->
          merge_arrays(nums1, nums2, i, j + 1, res ++ [Enum.at(nums2, j)])
        end
      end
    else
      res
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[[", "")
    temp = String.replace(temp, "]]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "]],[[")

    nums1 =
    for fld <- String.split(Enum.at(flds, 0), "],[") do
      for n <- String.split(fld, ",") do
        String.to_integer(n)
      end
    end

    nums2 =
      for fld <- String.split(Enum.at(flds, 1), "],[") do
        for n <- String.split(fld, ",") do
          String.to_integer(n)
        end
      end

    "nums1 = [" <> Mylib.intIntList_to_string(nums1) <> "], nums2 = [" <> Mylib.intIntList_to_string(nums2) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.merge_arrays(nums1, nums2)
      "result = [" <> Mylib.intIntList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
