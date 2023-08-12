defmodule Solution2 do
  # Time Limit Exceeded. 2402/2522
  @spec count_stepping_numbers(low :: String.t, high :: String.t) :: integer
  def count_stepping_numbers(low, high) do
    low = String.duplicate("0", String.length(high) - String.length(low)) <> low
    dfs(0, false, false, -1, false, String.to_charlist(low), String.to_charlist(high), 1_000_000_000 + 7)
  end

  @spec dfs(i :: integer, is_greater_thn_low :: bool, is_less_thn_high :: bool, prev_digit :: integer, nonzero :: bool, low :: [char], high :: [char], mod :: integer) :: integer
  def dfs(i, is_greater_thn_low, is_less_thn_high, prev_digit, nonzero, low, high, mod) do
    if i == Enum.count(high) do
      1
    else
      low_i = Enum.at(low, i) - ?0
      high_i = Enum.at(high, i) - ?0

      i_start =
        if is_greater_thn_low == false do
          low_i
        else
          0
        end

      i_end =
        if is_less_thn_high == false do
          high_i + 1
        else
          10
        end

      total =
        Enum.reduce(i_start..i_end-1, 0, fn nx_digit, total ->
          if nonzero == false or abs(prev_digit - nx_digit) == 1 do
            total + dfs(i + 1,
              is_greater_thn_low or (nx_digit > low_i),
              is_less_thn_high or (nx_digit < high_i),
              nx_digit, nonzero or (nx_digit != 0),
              low, high, mod)
          else
            total
          end
        end)
      rem(total, mod)
    end
  end

  # Time Limit Exceeded. 2402/2522
  @spec count_stepping_numbers2(low :: String.t, high :: String.t) :: integer
  def count_stepping_numbers2(low, high) do
    low = String.duplicate("0", String.length(high) - String.length(low)) <> low
    dfs2(0, false, false, -1, false, low, high, 1_000_000_000 + 7)
  end

  @spec dfs2(i :: integer, is_greater_thn_low :: bool, is_less_thn_high :: bool, prev_digit :: integer, nonzero :: bool, low :: String.t, high :: String.t, mod :: integer) :: integer
  def dfs2(i, is_greater_thn_low, is_less_thn_high, prev_digit, nonzero, low, high, mod) do
    if i == String.length(high) do
      1
    else
      i_start =
        if is_greater_thn_low == false do
          String.to_integer(String.at(low, i))
        else
          0
        end

      i_end =
        if is_less_thn_high == false do
          String.to_integer(String.at(high, i)) + 1
        else
          10
        end
      total =
        Enum.reduce(i_start..i_end-1, 0, fn nx_digit, total ->
          if nonzero == false or abs(prev_digit - nx_digit) == 1 do
            total + dfs2(i + 1,
              is_greater_thn_low or (nx_digit > String.to_integer(String.at(low, i))),
              is_less_thn_high or (nx_digit < String.to_integer(String.at(high, i))),
              nx_digit, nonzero or (nx_digit != 0),
              low, high, mod)
          else
            total
          end
        end)
      rem(total, mod)
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
