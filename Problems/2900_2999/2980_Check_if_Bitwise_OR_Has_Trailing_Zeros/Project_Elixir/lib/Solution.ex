defmodule Solution do
  # 359ms - 388ms
  @spec has_trailing_zeros(nums :: [integer]) :: boolean
  def has_trailing_zeros(nums) do
    Enum.reduce_while(nums, {0, false}, fn num, {cnt, _res} ->
      if rem(num, 2) == 0 do
        if cnt + 1 == 2 do
          {:halt, {cnt + 1, true}}
        else
          {:cont, {cnt + 1, false}}
        end
      else
        {:cont, {cnt, false}}
      end
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.has_trailing_zeros(nums)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
