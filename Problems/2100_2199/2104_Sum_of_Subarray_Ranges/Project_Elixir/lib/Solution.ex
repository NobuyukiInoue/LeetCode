defmodule Solution do
  # 545ms - 570ms
  @spec sub_array_ranges(nums :: [integer]) :: integer
  def sub_array_ranges(nums) do
    sub_array_ranges(nums, 0)
  end

  @spec sub_array_ranges(nums :: [integer], res :: integer) :: integer
  def sub_array_ranges([head | tail], res) do
    {res, _, _} =
      tail |>
        Enum.reduce({res, head, head}, fn num, {res, l, r} ->
          l = min(l, num)
          r = max(r, num)
          {res + (r - l), l, r}
        end)
    sub_array_ranges(tail, res)
  end

  def sub_array_ranges([], res) do
    res
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sub_array_ranges(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
