defmodule Solution do
  # 263ms - 269ms
  @spec h_index(citations :: [integer]) :: integer
  def h_index(citations) do
    n = Enum.count(citations)
    h_index(citations, n, 0, n)
  end

  @spec h_index(citations :: [integer], n :: integer, low :: integer, high :: integer) :: integer
  def h_index(citations, n, low, high) when low < high do
    mid = div(low + high, 2)
    k = n - mid
#   "mid = " <> Integer.to_string(mid) <> ", k = " <> Integer.to_string(k) |> IO.puts()
    cond do
    k > Enum.at(citations, mid) ->
      h_index(citations, n, mid + 1, high)
    mid == 0 or k < Enum.at(citations, mid - 1) ->
      h_index(citations, n, low, mid)
    true ->
      k
    end
  end

  def h_index(_, n, low, _) do
    n - low
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    citations = for n <- String.split(flds, ",") do String.to_integer(n) end
    "citations = [" <> Mylib.intList_to_string(citations) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.h_index(citations)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
