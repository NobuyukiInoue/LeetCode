defmodule Solution do
  # 281ms - 314ms
  @spec maximum_count(nums :: [integer]) :: integer
  def maximum_count(nums) do
    maximum_count(nums, 0, 0)
  end

  @spec maximum_count(nums :: [integer], pos :: integer(), neg :: integer) :: integer
  def maximum_count([], pos, neg) do
    Enum.max([pos, neg])
  end

  def maximum_count([head | tail], pos, neg) do
    cond do
      head > 0 ->
        maximum_count(tail, pos + 1, neg)
      head < 0 ->
        maximum_count(tail, pos, neg + 1)
      true ->
        maximum_count(tail, pos, neg)
    end
  end

  def maximum_count_use_reduce(nums) do
    # 300ms - 378ms
    nums
    |> Enum.reduce([0, 0], fn item, [less, more] ->
        cond do
            item < 0 -> [less + 1, more]
            item > 0 -> [less, more + 1]
            true -> [less, more]
        end
    end)
    |> Enum.max
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts

    exectime = Benchmark.measure(fn ->
      result = Solution.maximum_count(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
