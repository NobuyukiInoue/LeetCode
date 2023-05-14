defmodule Solution do
  # 657ms - 672ms
  @spec distinct_difference_array(nums :: [integer]) :: [integer]
  def distinct_difference_array(nums) do
    pref = Enum.reduce(nums, %{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)
    ans =
      Enum.reduce(nums, {[], pref, %{}}, fn num, {ans, pref, suff} ->
        suff = Map.put(suff, num, Map.get(suff, num, 0) + 1)
        pref = Map.put(pref, num, Map.get(pref, num, 0) - 1)
        pref =
        if Map.get(pref, num) == 0 do
          Map.delete(pref, num)
        else
          pref
        end
        {[Enum.count(suff) - Enum.count(pref) | ans], pref, suff}
      end) |> elem(0)
    Enum.reverse(ans)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.distinct_difference_array(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
