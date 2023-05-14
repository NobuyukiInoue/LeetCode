defmodule Solution do
  # 326ms - 350ms
  @spec triangular_sum(nums :: [integer]) :: integer
  def triangular_sum(nums) do
    n = Enum.count(nums) - 1
    nums |>
      Enum.reduce({0, 1, 0}, fn num, {i, nCr, res} ->
        {i + 1, div(nCr*(n - i), (i + 1)), rem(res + num*nCr, 10)}
      end) |> elem(2)
  end

## 1072ms - 1120ms
  def triangular_sum2(nums) do
    if Enum.count(nums) > 1 do
      nums =
        nums |>
          Enum.reduce({0, []}, fn num, {prev, res} ->
            {num, [rem(prev + num, 10) | res]}
          end) |> elem(1)
      triangular_sum2(Enum.reverse(nums) |> tl)
    else
      nums |> hd
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
      result = Solution.triangular_sum(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
