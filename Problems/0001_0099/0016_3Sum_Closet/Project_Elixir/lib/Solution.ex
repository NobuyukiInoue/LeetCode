defmodule Solution do
  # 385ms - 406ms
  @max 999_999
  @spec three_sum_closest(nums :: [integer], target :: integer) :: integer
  def three_sum_closest(nums, target) do
    nums
    |> Enum.sort()
    |> short_circ(target)
  end

  defp short_circ(l, target) do
    a = l |> Enum.take(3) |> Enum.sum()
    b = l |> Enum.reverse() |> Enum.take(3) |> Enum.sum()

    cond do
      a > target -> a
      b < target -> b
      true -> sum3(l, target, @max)
    end
  end

  defp sum3([_, _], _, min), do: min

  defp sum3([a | s], target, min) do
    b = sum2(s, Enum.reverse(s), target - a, Enum.count(s), @max)
    min = [a + b, min] |> Enum.min_by(fn q -> abs(q - target) end)

    if min == target do
      min
    else
      sum3(s, target, min)
    end
  end

  defp sum2([a | ta], [b | tb], target, size, min) do
    if size == 1 do
      sum2([a | ta], tb, target, 0, min)
    else
      min = [a + b, min] |> Enum.min_by(fn q -> abs(q - target) end)

      case a + b - target do
        0 -> a + b
        x when x > 0 -> sum2([a | ta], tb, target, size - 1, min)
        x when x < 0 -> sum2(ta, [b | tb], target, size - 1, min)
      end
    end
  end

  defp sum2(_, _, _, _, min), do: min

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")
    flds0 = String.split(Enum.at(flds, 0), ",")

    nums = for n <- flds0, do: n |> String.trim() |> String.to_integer()
    target = Enum.at(flds, 1) |> String.to_integer()
    "nums = [" <> Mylib.intList_to_string(nums) <> "], target = " <> Integer.to_string(target) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.three_sum_closest(nums, target)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
