defmodule Solution do
  # 338ms - 346ms
  @spec is_array_special(nums :: [integer]) :: boolean
  def is_array_special(nums) do
    Enum.reduce_while(nums |> tl, {nums |> hd, true}, fn num, {prev, _res} ->
      if rem(prev, 2) == rem(num, 2) do
        {:halt, {num, false}}
      else
        {:cont, {num, true}}
      end
    end)
    |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_array_special(nums)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
