defmodule Solution do
  # 638ms - 679ms
  @spec minimum_deletions(nums :: [integer]) :: integer
  def minimum_deletions(nums) do
    num0 = nums |> hd
    {_, {_min_v, min_p}, {_max_v, max_p}} =
      Enum.reduce(nums, {0, {num0, 0}, {num0, 0}}, fn num, {i, {min_v, min_p}, {max_v, max_p}} ->
        cond do
          num < min_v ->
            {i + 1, {num, i}, {max_v, max_p}}
          num > max_v ->
            {i + 1, {min_v, min_p}, {num, i}}
          true ->
            {i + 1, {min_v, min_p}, {max_v, max_p}}
        end
      end)
    {left, right} = {min(min_p, max_p), max(min_p, max_p)}
    n = Enum.count(nums)
    Enum.min([right + 1, n - left, left + 1 + (n - right)])
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_deletions(nums)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
