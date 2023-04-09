defmodule Solution do
  # 232ms - 263ms
  @spec split_num(num :: integer) :: integer
  def split_num(num) do
    nums = Integer.to_charlist(num)
    split_num(Enum.sort(nums), 0, 0, 0)
  end

  @spec split_num(nums :: [char], num1 :: integer, num2 :: integer, idx :: integer) :: integer
  def split_num([head | tail], num1, num2, idx) do
    if rem(idx, 2) == 0 do
      split_num(tail, num1*10 + (head - 0x30), num2, idx + 1)
    else
      split_num(tail, num1, num2*10 + (head - 0x30), idx + 1)
    end
  end

  def split_num([], num1, num2, _) do
    num1 + num2
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    num = String.to_integer(flds)
    "num = " <> Integer.to_string(num) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.split_num(num)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
