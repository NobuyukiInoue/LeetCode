defmodule Solution do
  # 317ms - 391ms
  @spec minimum_sum(nums :: [integer]) :: integer
  def minimum_sum(nums) do
    m = Enum.count(nums)
    ans =
      Enum.reduce(0..m-3, 512, fn i, ans ->
        Enum.reduce(i+1..m-2, ans, fn j, ans ->
          if Enum.at(nums, i) < Enum.at(nums, j) do
            Enum.reduce(j+1..m-1, ans, fn k, ans ->
              if Enum.at(nums, k) < Enum.at(nums, j) do
                Enum.min([ans, Enum.at(nums, i) + Enum.at(nums, j) + Enum.at(nums, k)])
              else
                ans
              end
            end)
          else
            ans
          end
        end)
      end)
    if ans == 512 do
      -1
    else
      ans
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
      result = Solution.minimum_sum(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
