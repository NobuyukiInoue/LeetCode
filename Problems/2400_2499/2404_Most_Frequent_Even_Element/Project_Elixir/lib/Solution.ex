defmodule Solution do
  # 512ms - 666ms
  @spec most_frequent_even(nums :: [integer]) :: integer
  def most_frequent_even(nums) do
    nums
    |> Enum.reduce(%{}, fn n, acc ->
      if rem(n, 2) == 0 do
        Map.update(acc, n, 1, &(&1 + 1))
      else
        acc
      end
    end)
    |> Enum.max_by(fn {k, v} -> {v, -k} end, fn -> {-1} end)
    |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.most_frequent_even(nums)
      "result = [" <> Integer.to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
