defmodule Solution do
  # 231ms - 238ms
  @spec nums_same_consec_diff(n :: integer, k :: integer) :: [integer]
  def nums_same_consec_diff(n, k) do
    Enum.reduce(1..9, [], fn i, res ->
      temp = df(i, n - 1, k, i)
      if temp != [], do: res ++ temp, else: res
    end)
  end

  @spec df(i :: integer, n :: integer, k :: integer, val :: integer) :: [integer]
  def df(_, n, _, val) when n == 0 do
    [val]
  end

  def df(i, n, k, val) do
    res1 = if i - k >= 0, do: df(i - k, n - 1, k, val*10 + i - k), else: []
    res2 = if k != 0 and i + k <= 9, do: df(i + k, n - 1, k, val*10 + i + k), else: []
    res1 ++ res2
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    n = Enum.at(flds, 0) |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()
    "n = " <> Integer.to_string(n) <> ", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.nums_same_consec_diff(n, k)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
