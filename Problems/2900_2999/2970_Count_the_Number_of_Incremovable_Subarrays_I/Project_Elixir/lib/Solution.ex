defmodule Solution do
  # 649ms - 785ms
  @spec incremovable_subarray_count(nums :: [integer]) :: integer
  def incremovable_subarray_count(nums) do
    n = Enum.count(nums)
    Enum.reduce(0..n-1, 0, fn i, ans ->
      Enum.reduce(i..n-1, ans, fn j, ans ->
        {_, ok, _} = Enum.reduce(nums, {0, true, -1}, fn num, {k, ok, lst} ->
          if k >= i and k <= j do
            {k + 1, ok, lst}
          else
            if lst < num do
              {k + 1, ok and true, num}
            else
              {k + 1, ok and false, num}
            end
          end
        end)
        if ok do
          ans + 1
        else
          ans
        end
      end)
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
      result = Solution.incremovable_subarray_count(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
