defmodule Solution do
  # 402ms - 475ms
  @spec max_sum(nums :: [integer]) :: integer
  def max_sum(nums) do
    Enum.reduce(nums, {-1, %{}}, fn num, {res, dic} ->
      max_digit = get_max_digit(num)
      val = Map.get(dic, max_digit)
      if val != nil do
        {max(res, num + val), Map.put(dic, max_digit, max(num, val))}
      else
        {res, Map.put(dic, max_digit, num)}
      end
    end) |> elem(0)
  end

  @spec get_max_digit(num :: integer) :: integer
  def get_max_digit(num) do
    get_max_digit(num, 0)
  end

  @spec get_max_digit(num :: integer, max_digit :: integer) :: integer
  def get_max_digit(num, max_digit) when num == 0 do
    max_digit
  end

  def get_max_digit(num, max_digit) do
    get_max_digit(div(num, 10), max(max_digit, rem(num, 10)))
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_sum(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
