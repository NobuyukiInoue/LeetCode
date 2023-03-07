defmodule Solution do
  # 436ms - 447ms
  @spec reduction_operations(nums :: [integer]) :: integer
  def reduction_operations(nums) do
    n_nums = Enum.sort(nums)
    reduction_operations(n_nums |> tl, n_nums |> hd , 0, 0)
  end

  @spec reduction_operations(nums :: [integer], prev :: integer, ans :: integer, cnt :: integer) :: integer
  def reduction_operations([head | tail], prev, ans, cnt) when head > prev do
    reduction_operations(tail, head, ans + cnt + 1, cnt + 1)
  end

  def reduction_operations([head | tail], _, ans, cnt) do
    reduction_operations(tail, head, ans + cnt, cnt)
  end

  def reduction_operations([], _, ans, _) do
    ans
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.reduction_operations(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
