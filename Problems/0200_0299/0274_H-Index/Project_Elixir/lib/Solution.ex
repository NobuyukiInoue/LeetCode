defmodule Solution do
  # 214ms - 239ms
  @spec h_index(citations :: [integer]) :: integer
  def h_index(citations) do
    h_index(Enum.sort(citations), Enum.count(citations), 0)
  end

  @spec h_index(citations :: [integer], n :: integer, i :: integer) :: integer
  def h_index([head | tail], n, i) when i < n and n - i > head do
      h_index(tail, n, i + 1)
  end

  def h_index(_, n, i) do
    n - i
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
