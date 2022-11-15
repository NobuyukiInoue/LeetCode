defmodule Solution do
  # 407ms - 442ms
  @spec average_value(nums :: [integer]) :: integer
  def average_value(nums) do
    average_value(nums, 0, 0)
  end

  @spec average_value(nums :: [integer], count :: integer, total :: integer) :: integer
  def average_value(nums, count, total) do
    if nums != [] do
      if rem(Enum.at(nums, 0), 6) == 0 do
        average_value(nums |> tl, count + 1, total + Enum.at(nums, 0))
      else
        average_value(nums |> tl, count, total)
      end
    else
      if count > 0 do
        div(total, count)
      else
        0
      end
    end
  end

@spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.average_value(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
