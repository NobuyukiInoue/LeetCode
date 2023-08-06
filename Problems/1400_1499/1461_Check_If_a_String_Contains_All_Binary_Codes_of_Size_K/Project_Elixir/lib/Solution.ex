defmodule Solution do
  # 2077ms - 2216ms
  @spec has_all_codes(s :: String.t(), k :: integer) :: boolean
  def has_all_codes(s, k) do
    s
    |> String.graphemes()
    |> aux(:queue.new(), 0, MapSet.new(), k)
    |> MapSet.size()
    |> then(&(&1 == 2**k))
  end

  def aux([], q, k, set, k) do
    MapSet.put(set, :queue.to_list(q))
  end

  def aux([], _, _, set, _) do
    set
  end

  def aux([x | xs], q, k, set, k) do
    aux(xs, :queue.in(x, :queue.drop(q)), k, MapSet.put(set, :queue.to_list(q)), k)
  end

  def aux([x | xs], q, len, set, k) do
    aux(xs, :queue.in(x, q), len + 1, set, k)
  end

  # 2284ms - 2401ms
  @spec has_all_codes2(s :: String.t, k :: integer) :: boolean
  def has_all_codes2(s, k) do
    limit = Integer.pow(2, k)
    s
    |> String.graphemes()
    |> Enum.chunk_every(k, 1, :discard)
    |> Enum.reduce(MapSet.new(), fn chnk, set ->
      MapSet.put(set, chnk)
    end)
    |> MapSet.size()
    |> Kernel.==(limit)
  end

  # Time Limit Exceeded. 103/201
  @spec has_all_codes3(s :: String.t, k :: integer) :: boolean
  def has_all_codes3(s, k) do
    codes =
      Enum.reduce(0..String.length(s) - k, %{}, fn i, codes ->
        Map.put(codes, String.slice(s, i, k), true)
      end)
#   Enum.map(codes, fn {k, v} -> "k = " <> k <> ", v = " <> to_string(v) |> IO.puts() end)
    Enum.count(codes) == 2**k
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    s = Enum.at(flds, 0)
    k = String.to_integer(Enum.at(flds, 1))
    "s = \"" <>  s <> "\", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.has_all_codes(s, k)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
