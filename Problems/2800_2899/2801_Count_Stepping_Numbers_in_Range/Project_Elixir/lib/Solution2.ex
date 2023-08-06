defmodule Solution2 do
  # Time Limit Exceeded. 2402/2522
  @spec count_stepping_numbers(low :: String.t, high :: String.t) :: integer
  def count_stepping_numbers(low, high) do
    low = String.duplicate("0", String.length(high) - String.length(low)) <> low
    args = %{l: low, h: high, m: 1_000_000_000 + 7}
    dfs(0, false, false, -1, false, args)
  end

  @spec dfs(i :: integer, is_greater_thn_low :: bool, is_less_thn_high :: bool, prev_digit :: integer, nonzero :: bool, args :: {}) :: integer
  defp dfs(i, is_greater_thn_low, is_less_thn_high, prev_digit, nonzero, args) do
    if i == String.length(args[:h]) do
      1
    else
      i_start =
        if is_greater_thn_low == false do
          String.to_integer(String.at(args[:l], i))
        else
          0
        end

      i_end =
        if is_less_thn_high == false do
          String.to_integer(String.at(args[:h], i)) + 1
        else
          10
        end
      total =
        Enum.reduce(i_start..i_end-1, 0, fn nx_digit, total ->
          if nonzero == false or abs(prev_digit - nx_digit) == 1 do
            total + dfs(i + 1, is_greater_thn_low or (nx_digit > String.to_integer(String.at(args[:l], i))),
              is_less_thn_high or (nx_digit < String.to_integer(String.at(args[:h], i))),
              nx_digit, nonzero or (nx_digit != 0), args)
          else
            total
          end
        end)
      rem(total, args[:m])
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    low = Enum.at(flds, 0)
    high = Enum.at(flds, 1)
    "low = " <>  low <> ", high = " <> high |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_stepping_numbers(low, high)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
