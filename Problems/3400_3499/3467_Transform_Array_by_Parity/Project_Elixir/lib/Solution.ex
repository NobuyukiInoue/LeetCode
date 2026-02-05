defmodule Solution do
  # 2ms
  @spec transform_array(nums :: [integer]) :: [integer]
  def transform_array(nums) do
    cnt_even = nums |> Enum.filter(fn x -> rem(x, 2) == 0 end) |> Enum.count
    cnt_odd = Enum.count(nums) - cnt_even
    l1 =
      if cnt_even > 0 do
        for _ <- 1..cnt_even do 0 end
      else
        []
      end
    l2 =
      if cnt_odd > 0 do
        for _ <- 1..cnt_odd do 1 end
      else
        []
      end
    l1 ++ l2
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.transform_array(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
