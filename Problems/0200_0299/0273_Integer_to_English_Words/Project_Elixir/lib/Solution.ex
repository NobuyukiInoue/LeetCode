defmodule Solution do
  # 306ms - 335ms
  @spec number_to_words(num :: integer) :: String.t
  def number_to_words(num) when num == 0 do
    "Zero"
  end

  def number_to_words(num) do
    ones = ["", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
    tens = ["", " Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
    thousands = ["", " Thousand", " Million", " Billion"]
    String.trim(helper(num, ones, tens, thousands))
  end

  @spec helper(n :: integer, ones :: [String.t], tens :: [String.t], thousands :: [String.t]) :: String.t
  def helper(n, ones, _tens, _thousands) when n < 20 do
    Enum.at(ones, n)
  end

  def helper(n, ones, tens, thousands) when n < 100 do
    Enum.at(tens, div(n, 10)) <> helper(rem(n, 10), ones, tens, thousands)
  end

  def helper(n, ones, tens, thousands) when n < 1000 do
    helper(div(n, 100), ones, tens, thousands) <> " Hundred" <> helper(rem(n, 100), ones, tens, thousands)
  end

  def helper(n, ones, tens, thousands) do
    Enum.reduce_while(3..0, "", fn i, _ ->
      if n >= 1000**i do
        {:halt, helper(div(n, 1000**i), ones, tens, thousands) <> Enum.at(thousands, i) <> helper(rem(n, 1000**i), ones, tens, thousands)}
      else
        {:cont, ""}
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")
    num = String.to_integer(flds)
    "num = " <> to_string(num) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.number_to_words(num)
      "result = \"" <> result <> "\"" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
