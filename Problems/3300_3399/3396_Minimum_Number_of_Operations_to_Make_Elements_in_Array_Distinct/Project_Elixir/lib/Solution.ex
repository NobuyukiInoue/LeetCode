defmodule Solution do
  # 5ms - 9ms
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    Enum.reduce_while(nums |> Enum.reverse(), {Enum.count(nums) - 1, [], 0}, fn num, {i, cnts, _res} ->
      if Enum.find(cnts, fn x -> x == num end) == nil do
        {:cont, {i - 1, [num] ++ cnts, 0}}
      else
        {:halt, {i - 1, cnts, div(i, 3) + 1}}
      end
    end)
    |> elem(2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_operations(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
