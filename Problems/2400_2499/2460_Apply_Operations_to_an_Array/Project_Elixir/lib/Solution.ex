defmodule Solution do
  # 401ms - 418ms
  @spec apply_operations(nums :: [integer]) :: [integer]
  def apply_operations(nums) do
    apply_operations(nums, [], [])
  end

  def apply_operations([], xs, ys) do
    Enum.reverse(xs) ++ ys
  end

  def apply_operations([x], xs, ys) do
    apply_operations([], [x | xs], ys)
  end

  def apply_operations([a, b | rs], xs, ys) do
    cond do
      a == 0 -> apply_operations([b | rs], xs, [0 | ys])
      a == b -> apply_operations(rs, [2 * a | xs], [0 | ys])
      true -> apply_operations([b | rs], [a | xs], ys)
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
      result = Solution.apply_operations(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
