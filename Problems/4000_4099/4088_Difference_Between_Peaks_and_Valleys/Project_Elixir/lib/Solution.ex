defmodule Solution do
  # 16ms
  @spec peak_valley_difference(nums :: [integer]) :: integer
  def peak_valley_difference(nums) when length(nums) < 3, do: 0
  def peak_valley_difference(nums) do
    nums
    |> Stream.chunk_every(3, 1, :discard)
    |> Enum.reduce(0, fn [prev, curr, nxt], acc ->
      cond do
        prev < curr and curr > nxt -> acc + curr
        prev > curr and curr < nxt -> acc - curr
        true -> acc
      end
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
      result = Solution.peak_valley_difference(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
