defmodule Solution do
  # 217ms - 252ms
  @spec str_str(haystack :: String.t, needle :: String.t) :: integer
  def str_str(haystack, needle) do
    str_str(String.to_charlist(haystack), String.to_charlist(needle), 0)
  end

  @spec str_str(haystack :: [char], needle :: [char], idx :: integer) :: integer
  def str_str([h_head | h_tail], [n_head | n_tail], idx) when h_head == n_head do
    if Enum.count(h_tail) >= Enum.count(n_tail) do
      if check(h_tail, n_tail, 0) == true do
        idx
      else
        str_str(h_tail, [n_head | n_tail], idx + 1)
      end
    else
      -1
    end
  end

  def str_str([_ | h_tail], [n_head | n_tail], idx) do
    str_str(h_tail, [n_head | n_tail], idx + 1)
  end

  def str_str([], _,  _) do
    -1
  end

  @spec check(haystack :: [char], needle :: [char], cnt :: integer) :: bool
  def check([h_head | h_tail], [n_head | n_tail], cnt) when h_head == n_head  do
    check(h_tail, n_tail, cnt + 1)
  end

  def check(_, [], _) do
    true
  end

  def check(_, _, _) do
    false
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, "],[")
    haystack = Enum.at(flds, 0)
    needle = Enum.at(flds,1)
    "haystack = \"" <> haystack <> "\"" <> ", needle = " <> needle <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.str_str(haystack, needle)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
