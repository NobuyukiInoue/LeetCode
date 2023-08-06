defmodule Solution do
  # 365ms - 387ms
  @spec is_good(nums :: [integer]) :: boolean
  def is_good(nums) do
    nums = Enum.sort(nums)
    res =
      Enum.reduce_while(1..Enum.count(nums)-1, {Enum.at(nums, 0), true}, fn i, {prev, _} ->
        cur = Enum.at(nums, i)
        if cur != prev + 1 do
          {:halt, {cur, false}}
        else
          {:cont, {cur, true}}
        end
      end)
    cond do
      res == false ->
        false
      Enum.at(nums, -1) == Enum.count(nums) - 1 and Enum.at(nums, -2) == Enum.at(nums, -1) ->
        true
      true ->
        false
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
      result = Solution.is_good(nums)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
