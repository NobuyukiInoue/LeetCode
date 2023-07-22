defmodule Solution do
  @spec partition_array(nums :: [integer], k :: integer) :: integer
  # 442ms - 541ms
  def partition_array(nums, k) do
    nums
    |> Enum.sort()
    |> then(&aux(&1, hd(&1), k, 1))
  end

  def aux([], _m, _k, ct), do: ct
  def aux([n | ns], m, k, ct) when n - m <= k, do: aux(ns, m, k, ct)
  def aux([n | ns], _m, k, ct), do: aux(ns, n, k, ct + 1)

  @spec partition_array2(nums :: [integer], k :: integer) :: integer
  # Time Limit Exceeded. 70/92
  def partition_array2(nums, k) do
    len_nums = Enum.count(nums)
    if len_nums == 1 do
      1
    else
      nums = Enum.sort(nums)
      Enum.reduce(1..len_nums - 1, {1, Enum.at(nums, 0)}, fn i, {ans, start} ->
        cur = Enum.at(nums, i)
        diff = cur - start
        if diff > k do
          {ans + 1, cur}
        else
          {ans, start}
        end
      end) |> elem(0)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()
    "nums = [" <>  Mylib.intList_to_string(nums) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.partition_array(nums, k)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
