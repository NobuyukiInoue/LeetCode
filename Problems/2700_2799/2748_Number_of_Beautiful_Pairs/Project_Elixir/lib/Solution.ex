defmodule Solution do
  # 818ms - 867ms
  @spec count_beautiful_pairs(nums :: [integer]) :: integer
  def count_beautiful_pairs(nums) do
    Enum.reduce(1..Enum.count(nums)-1, 0, fn i, ans ->
      m = rem(Enum.at(nums, i), 10)
      Enum.reduce(0..i-1, ans, fn j, ans ->
        if Integer.gcd(m, n_div_10(Enum.at(nums, j))) == 1 do
          ans + 1
        else
          ans
        end
      end)
    end)
  end

  @spec n_div_10(n :: integer) :: integer
  def n_div_10(n) when n < 10 do
    n
  end

  def n_div_10(n) do
    n_div_10(div(n, 10))
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_beautiful_pairs(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
