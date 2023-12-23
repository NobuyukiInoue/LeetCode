defmodule Solution do
  # 305ms - 315ms
  @spec k_closest(points :: [[integer]], k :: integer) :: [[integer]]
  def k_closest(points, k) do
    points
      |> Enum.reduce([], fn p, res ->
        [x | tail] = p
        y = tail |> hd
        [[x*x + y*y, x, y]] ++ res
      end)
      |> Enum.reverse()
      |> Enum.sort()
      |> Enum.reduce_while({0, []}, fn res, {i, ans} ->
        if i == k do
          {:halt, {i + 1, ans}}
        else
          {:cont, {i + 1, [res |> tl] ++ ans}}
        end
      end)
      |> elem(1)
      |> Enum.reverse()
  end

  # 329ms - 372ms
  @spec k_closest2(points :: [[integer]], k :: integer) :: [[integer]]
  def k_closest2(points, k) do
    dists = Enum.reduce(points, [], fn p, res ->
      [x | tail] = p
      y = tail |> hd
      [[x*x + y*y, x, y]] ++ res
    end) |> Enum.reverse() |> Enum.sort()
    Enum.reduce_while(dists, {0, []}, fn res, {i, ans} ->
      if i == k do
        {:halt, {i + 1, ans}}
      else
        {:cont, {i + 1, [res |> tl] ++ ans}}
      end
    end)
    |> elem(1) |> Enum.reverse()
  end

#
#  def k_closest(points, k) do
#    pq = Enum.reduce(points, PriorityQueue.new(), fn p, pq ->
#      [x | y] = p
#      dist = x*x + y*y
#      PriorityQueue.put(pq, {dist, [x, y]})
#    end)
#    Enum.reduce(pq, {0, []}, fn p, {i, ans} ->
#     {i + 1, PriorityQueue.pop(p)}
#    end) |> elem(1)
#  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[[", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "]],[")

    points =
    for fld <- String.split(Enum.at(flds, 0), "],[") do
      for n <- String.split(fld, ",") do
        String.to_integer(n)
      end
    end

    k = Enum.at(flds, 1) |> String.replace("]]", "") |> String.to_integer()
    "points = [" <> Mylib.intIntList_to_string(points) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.k_closest(points, k)
      "result = " <> Mylib.intIntList_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
