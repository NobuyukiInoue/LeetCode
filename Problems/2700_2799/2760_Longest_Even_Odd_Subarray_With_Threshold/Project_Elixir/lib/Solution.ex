import Bitwise

defmodule Solution do
  # 957ms - 1077ms
  @spec longest_alternating_subarray(nums :: [integer], threshold :: integer) :: integer
  def longest_alternating_subarray(nums, threshold) do
    nums |> Enum.reduce({0, 0, 0}, fn num, {ans, cnt, parity} ->
      {parity, cnt} =
      cond do
        num > threshold ->
          {parity, 0}
        cnt >= 1 and parity != rem(num, 2) ->
          {bxor(parity, 1), cnt + 1}
        true ->
          parity = rem(num, 2)
          {parity, bxor(parity, 1)}
      end
      {max(ans, cnt), cnt, parity}
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    threshold = Enum.at(flds, 1) |> String.to_integer()
    "nums = [" <>  Mylib.intList_to_string(nums) <> "], threshold = " <> Integer.to_string(threshold) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.longest_alternating_subarray(nums, threshold)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
