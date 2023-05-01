defmodule Solution do
  @spec maximize_sum(nums :: [integer], k :: integer) :: integer
  def maximize_sum(nums, k) do
    # 567ms - 580ms
    Enum.max(nums)*k + div((k - 1)*k, 2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()
    "nums = [" <>  Mylib.intList_to_string(nums) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.maximize_sum(nums, k)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
