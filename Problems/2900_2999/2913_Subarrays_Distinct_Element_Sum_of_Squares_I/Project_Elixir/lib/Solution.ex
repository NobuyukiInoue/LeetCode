defmodule Solution do
  # 770ms - 795ms
  @spec sum_counts(nums :: [integer]) :: integer
  def sum_counts(nums) do
    m = Enum.count(nums)
    Enum.reduce(0..m-1, 0, fn i, ans ->
      Enum.reduce(i..m-1, ans, fn j, ans ->
        temp = MapSet.size(MapSet.new(Enum.slice(nums, i..j)))
        ans + temp*temp
      end)
    end)
  end

  # 799ms - 817ms
  def sum_counts2(nums) do
    m = length(nums)
    for chunk_size <- 1..m, reduce: 0 do
      acc ->
        Enum.chunk_every(nums, chunk_size, 1, :discard)
        |> Enum.reduce(0, fn chunk, acc ->
          chunk
          |> MapSet.new()
          |> MapSet.size()
          |> then(&(&1 * &1 + acc))
        end)
        |> then(&(&1 + acc))
    end  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sum_counts(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
