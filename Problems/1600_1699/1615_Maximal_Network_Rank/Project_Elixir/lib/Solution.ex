defmodule Solution do
  # 180ms - 185ms
  @spec maximal_network_rank(n :: integer, roads :: [[integer]]) :: integer
  def maximal_network_rank(n, roads) do
    connections =
      Enum.reduce(0..n-1, %{}, fn i, connections ->
        Map.put(connections, i, 0)
      end)
    graph =
      Enum.reduce(0..n-1, %{}, fn i, graph ->
        Enum.reduce(0..n-1, graph, fn j, graph ->
          Map.put(graph, {i, j}, false)
        end)
      end)
    {connections, graph} =
      Enum.reduce(roads, {connections, graph}, fn [a, b], {connections, graph} ->
        connections = Map.put(connections, a, connections[a] + 1)
        connections = Map.put(connections, b, connections[b] + 1)
        graph = Map.put(graph, {a, b}, true)
        graph = Map.put(graph, {b, a}, true)
        {connections, graph}
      end)
    Enum.reduce(0..n-1, 0, fn i, max_rank ->
      if i + 1 == n do
        max_rank
      else
        Enum.reduce(i+1..n-1, max_rank, fn j, max_rank ->
          rank =
            if graph[{i, j}] do
              connections[i] + connections[j] - 1
            else
              connections[i] + connections[j]
            end
          max(max_rank, rank)
        end)
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "]]]", "")
    flds = String.split(temp, "],[[")

    n = String.replace(Enum.at(flds, 0), "[[", "") |> String.to_integer()
    roads =
    for row <- String.split(Enum.at(flds, 1), "],[") do
      for col <- String.split(row, ",") do
        String.to_integer(col)
      end
    end

    "n = " <> Integer.to_string(n) <> ", roads = [" <> Mylib.intIntList_to_string(roads) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.maximal_network_rank(n, roads)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
