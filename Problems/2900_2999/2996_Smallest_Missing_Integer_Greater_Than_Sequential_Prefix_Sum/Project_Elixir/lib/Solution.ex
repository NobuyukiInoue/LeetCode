defmodule Solution do
  # 295ms - 363ms
  @spec missing_integer(nums :: [integer]) :: integer
  def missing_integer(nums) do
    prev = nums |> hd
    total = Enum.reduce_while(nums |> tl, {prev, prev}, fn num, {prev, total} ->
        if prev + 1 == num do
          {:cont, {num, total + num}}
        else
          {:halt, {num, total}}
        end
    end) |> elem(1)
    Enum.reduce(Enum.sort(nums), total, fn num, total ->
      if num == total do
        total + 1
      else
        total
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.missing_integer(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
