defmodule Solution do
  # 312ms - 353ms
  @spec return_to_boundary_count(nums :: [integer]) :: integer
  def return_to_boundary_count(nums) do
    Enum.reduce(nums, {0, 0}, fn num, {ans, pos} ->
      pos = pos + num
      if pos == 0 do
        {ans + 1, pos}
      else
        {ans, pos}
      end
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.return_to_boundary_count(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
