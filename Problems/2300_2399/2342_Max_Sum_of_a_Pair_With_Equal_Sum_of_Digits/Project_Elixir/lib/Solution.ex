defmodule Solution do
  # 450ms - 475ms
  @spec maximum_sum(nums :: [integer]) :: integer
  def maximum_sum(nums) do
    maximum_sum(nums, %{}, -1)
  end

  @spec maximum_sum(nums :: [integer], map :: %{}, max_val :: integer) :: integer
  def maximum_sum([head | tail], map, max_val) do
    digits_sum = get_digits_sum(head, 0)
    if Map.get(map, digits_sum) == nil do
      maximum_sum(tail, Map.put(map, digits_sum, head), max_val)
    else
      new_max_val = head + Map.get(map, digits_sum)
      max_val = max(new_max_val, max_val)
      maximum_sum(tail, Map.put(map, digits_sum, max(head, Map.get(map, digits_sum))), max_val)
    end
  end

  def maximum_sum([], _, max_val) do
    max_val
  end

  @spec get_digits_sum(num :: integer, digits_sum :: integer) :: integer
  def get_digits_sum(num, digits_sum) when num > 0 do
    get_digits_sum(div(num, 10), digits_sum +  rem(num, 10))
  end

  def get_digits_sum(_, digits_sum) do
    digits_sum
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.maximum_sum(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
