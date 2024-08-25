defmodule Solution do
  # 369ms - 383ms
  @spec get_final_state(nums :: [integer], k :: integer, multiplier :: integer) :: [integer]
  def get_final_state(nums, k, _multiplier) when k == 0 do
    nums
  end

  def get_final_state(nums, k, multiplier) do
    {_, n, v_min} =
      Enum.reduce(nums, {0, 0, nums |> hd}, fn num, {i, n, v_min} ->
        if num < v_min do
          {i + 1, i, num}
        else
          {i + 1, n, v_min}
        end
      end)
    get_final_state(List.replace_at(nums, n, v_min*multiplier), k - 1, multiplier)
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
    multiplier = String.to_integer(Enum.at(flds, 2))
    "nums = [" <> Mylib.intList_to_string(nums) <> "], k = " <> Integer.to_string(k) <> ", multiplier = " <> Integer.to_string(multiplier) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.get_final_state(nums, k, multiplier)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
