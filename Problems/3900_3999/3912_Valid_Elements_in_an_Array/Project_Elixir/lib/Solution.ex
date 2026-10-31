defmodule Solution do
  # 1ms
  @spec find_valid_elements(nums :: [integer]) :: [integer]
  def find_valid_elements(nums) do
    initial_state = {[0], [:infinity]}
    {nums_l, nums_r} =
      Enum.reduce(nums, initial_state, fn num, {l, r} ->
        updated_r = drop_while_less_equal(r, num)
        if num > hd(l) do
          {[num | l], updated_r}
        else
          {l, [num | updated_r]}
        end
      end)
    final_l = nums_l |> Enum.reverse() |> tl()
    final_r = nums_r |> Enum.reverse() |> tl()
    final_l ++ final_r
  end

  defp drop_while_less_equal([head | tail], num) when num >= head do
    drop_while_less_equal(tail, num)
  end
  defp drop_while_less_equal(r, _num), do: r

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_valid_elements(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
