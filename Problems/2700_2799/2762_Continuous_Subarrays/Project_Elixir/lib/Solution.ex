defmodule Solution do
  # 1202ms - 1416ms
  @spec continuous_subarrays(nums :: [integer]) :: integer
  def continuous_subarrays(nums) do
    Enum.reduce(nums, {0, 0, %{}, 0}, fn num, {i, j, dic, ans} ->
      {i, dic} =
        Enum.reduce(Map.keys(dic), {i, dic}, fn k, {i, dic} ->
          if abs(k - num) > 2 do
            {max(i, dic[k] + 1), Map.delete(dic, k)}
          else
            {i, dic}
          end
        end)
      {i, j + 1, Map.put(dic, num, j), ans + (j - i + 1)}
    end)
    |> elem(3)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.continuous_subarrays(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
