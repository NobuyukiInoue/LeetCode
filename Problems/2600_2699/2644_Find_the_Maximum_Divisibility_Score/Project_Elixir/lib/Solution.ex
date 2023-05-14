defmodule Solution do
  # 1857ms - 1949ms
  @spec max_div_score(nums :: [integer], divisors :: [integer]) :: integer
  def max_div_score(nums, divisors) do
    divisors |>
      Enum.reduce({-1, -1}, fn divisor, {ans, max_cnt} ->
        cnt =
          Enum.reduce(nums, 0, fn num, cnt ->
            if rem(num, divisor) == 0 do
              cnt + 1
            else
              cnt
            end
          end)
        cond do
          cnt > max_cnt ->
            {divisor, cnt}
          cnt == max_cnt ->
            {min(ans, divisor), cnt}
          true ->
            {ans, max_cnt}
        end
      end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums =
      for n <- String.split(Enum.at(flds, 0), ",") do
        String.to_integer(n)
      end

    divisors =
      for n <- String.split(Enum.at(flds, 1), ",") do
        String.to_integer(n)
      end

    "nums = [" <> Mylib.intList_to_string(nums) <> "], divisors = [" <> Mylib.intList_to_string(divisors) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_div_score(nums, divisors)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
