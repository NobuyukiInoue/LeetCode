defmodule Solution do
  # 285ms - 297ms
  @spec find_prefix_score(nums :: [integer]) :: [integer]
  def find_prefix_score(nums) do
    Enum.reduce(nums, {0, [0]}, fn num, {t_max, ans} ->
      t_max = max(t_max, num)
      {t_max, [num + t_max + (ans |> hd) | ans]}
    end) |> elem(1) |> Enum.reverse() |> tl
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_prefix_score(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
