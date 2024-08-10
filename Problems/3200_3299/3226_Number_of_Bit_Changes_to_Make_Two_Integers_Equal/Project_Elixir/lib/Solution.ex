defmodule Solution do
  # 299ms - 348ms
  @spec min_changes(n :: integer, k :: integer) :: integer
  def min_changes(n, k) do
    min_changes(n, k, 0)
  end

  @spec min_changes(n :: integer, k :: integer, cnt :: integer) :: integer
  def min_changes(n, k, cnt) when n > 0 or k > 0 do
    {m_n, m_k} = {rem(n, 2), rem(k, 2)}
    cond do
      m_n == 1 and m_k == 0 ->
        min_changes(div(n, 2), div(k, 2), cnt + 1)
      m_n == 0 and m_k == 1 ->
        -1
      true ->
        min_changes(div(n, 2), div(k, 2), cnt)
    end
  end

  def min_changes(_n, _k, cnt) do
    cnt
  end

  @spec loop_main(temp :: String.t) :: :oy
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    x = String.to_integer(Enum.at(flds, 0))
    y = String.to_integer(Enum.at(flds, 1))
    "x = " <> Integer.to_string(x) <> ", y = " <> Integer.to_string(y) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.min_changes(x, y)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
