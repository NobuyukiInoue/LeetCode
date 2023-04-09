use Bitwise

defmodule Solution do
  # 320ms - 331ms
  @spec even_odd_bit(n :: integer) :: [integer]
  def even_odd_bit(n) do
    even_odd_bit(n, [0, 0], false)
  end

  @spec even_odd_bit(n :: integer, ans :: [integer], odd :: boolean) :: [integer]
  def even_odd_bit(n, ans, odd) when n > 0 and odd == false do
    if (n &&& 1) == 1 do
      even_odd_bit(n >>> 1, [Enum.at(ans, 0) + 1, Enum.at(ans, 1)], true)
    else
      even_odd_bit(n >>> 1, ans, true)
    end
  end

  def even_odd_bit(n, ans, _) when n > 0 do
    if (n &&& 1) == 1 do
      even_odd_bit(n >>> 1, [Enum.at(ans, 0), Enum.at(ans, 1) + 1], false)
    else
      even_odd_bit(n >>> 1, ans, false)
    end
  end

  def even_odd_bit(_, ans, _) do
    ans
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")
    n = String.to_integer(flds)
    "n = " <> to_string(n) |> IO.puts()

    execright = Benchmark.measure(fn ->
      result = Solution.even_odd_bit(n)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(execright, 3)) <> " [s]\n" |> IO.puts()
  end
end
