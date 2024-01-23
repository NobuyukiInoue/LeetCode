defmodule Solution do
  # 396ms - 429ms
  @spec minimum_cost1(nums :: [integer]) :: integer
  def minimum_cost1(nums) do
    m_nums = Enum.reduce(nums, {0, Map.new()}, fn num, {i, m_nums} ->
      {i + 1, Map.put(m_nums, i, num)}
    end) |> elem(1)
    n = Enum.count(nums)
    Enum.reduce(1..n-2, 150, fn i, ans ->
      Enum.reduce(1..n-i-1, ans, fn j, ans ->
        min(ans, m_nums[0] + m_nums[i] + m_nums[i + j])
      end)
    end)
  end

  # 355ms - 396ms
  @spec minimum_cost(nums :: [integer]) :: integer
  def minimum_cost(nums) do
    tl_nums = Enum.sort(nums |> tl)
    (nums |> hd) + (tl_nums |> hd) + (tl_nums |> tl |> hd)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_cost(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
