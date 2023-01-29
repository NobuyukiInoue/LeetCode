defmodule Solution do
  # 333ms - 367ms
  @spec difference_of_sum(nums :: [integer]) :: integer
  def difference_of_sum(nums) do
    difference_of_sum(nums, 0, 0)
  end

  @spec difference_of_sum(nums :: [integer], ele :: integer, dig :: integer) :: integer
  def difference_of_sum([head | tail], ele, dig) when head >= 10 do
    difference_of_sum(tail, ele + head, calc_dig(dig, head))
  end

  def difference_of_sum([head | tail], ele, dig) do
    difference_of_sum(tail, ele + head, dig + head)
  end

  def difference_of_sum([], ele, dig) do
    ele - dig
  end

  @spec calc_dig(dig :: integer, num :: integer) :: integer
  def calc_dig(dig, num) when num > 0 do
    calc_dig(dig + rem(num, 10), div(num, 10))
  end

  def calc_dig(dig, _) do
    dig
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts

    exectime = Benchmark.measure(fn ->
      result = Solution.difference_of_sum(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
