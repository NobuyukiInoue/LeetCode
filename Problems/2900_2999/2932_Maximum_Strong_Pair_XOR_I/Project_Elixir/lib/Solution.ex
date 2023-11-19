defmodule Solution do
  # 293ms - 312ms
  @spec maximum_strong_pair_xor(nums :: [integer]) :: integer
  def maximum_strong_pair_xor(nums) do
    Enum.reduce(nums, 0, fn x, ans ->
      Enum.reduce(nums, ans, fn y, ans ->
        if abs(x - y) <= min(x, y) do
          max(ans, Bitwise.bxor(x, y))
        else
          ans
        end
      end)
    end)
  end

  # 324ms - 406ms
  @spec maximum_strong_pair_xor2(nums :: [integer]) :: integer
  def maximum_strong_pair_xor2(nums) do
    Enum.reduce(nums, {0, 0}, fn x, {i, ans} ->
      ans = Enum.reduce(Enum.slice(nums, i, Enum.count(nums) - i), ans, fn y, ans ->
        if abs(x - y) <= min(x, y) do
          max(ans, Bitwise.bxor(x, y))
        else
          ans
        end
      end)
      {i + 1, ans}
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
      result = Solution.maximum_strong_pair_xor(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
