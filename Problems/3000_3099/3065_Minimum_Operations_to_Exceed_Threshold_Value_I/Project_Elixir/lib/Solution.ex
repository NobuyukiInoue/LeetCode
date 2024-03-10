defmodule Solution do
  # 343ms - 383ms
  @spec min_operations1(nums :: [integer], k :: integer) :: integer
  def min_operations1(nums, k) do
    Enum.reduce(nums, 0, fn num, ans ->
      if num < k do
        ans + 1
      else
        ans
      end
    end)
  end

  # 347ms - 362ms
  @spec min_operations(nums :: [integer], k :: integer) :: integer
  def min_operations(nums, k) do
    nums
    |> Enum.filter(fn(num) -> num < k end)
    |> Enum.count
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

    "nums = " <> Mylib.intList_to_string(nums) <> ", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.min_operations(nums, k)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
