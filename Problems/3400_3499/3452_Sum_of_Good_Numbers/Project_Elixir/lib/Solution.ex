defmodule Solution do
  # 4ms
  @spec sum_of_good_numbers(nums :: [integer], k :: integer) :: integer
  def sum_of_good_numbers(nums, k) do
    n = nums |> Enum.count()
    Enum.reduce(nums, {0, 0}, fn num, {i, ans} ->
      cond do
        i + k < n and num <= Enum.at(nums, i + k) ->
          {i + 1, ans}
        0 <= i - k and num <= Enum.at(nums, i - k) ->
          {i + 1, ans}
        true ->
          {i + 1, ans + num}
      end
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums =
      for num <- String.split(Enum.at(flds, 0), ",") do
          String.to_integer(num)
      end

    k = String.to_integer(Enum.at(flds, 1))
    "nums = [" <> Mylib.intList_to_string(nums) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sum_of_good_numbers(nums, k)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
