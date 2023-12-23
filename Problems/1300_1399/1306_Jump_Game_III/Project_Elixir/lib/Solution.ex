defmodule Solution do
  # 377ms - 419ms
  @spec can_reach(arr :: [integer], start :: integer) :: boolean
  def can_reach(arr, start) do
    m_arr = Enum.reduce(arr, {0, %{}}, fn cur, {i, res} ->
      {i + 1, Map.put(res, i, cur)}
    end) |> elem(1)
    map_can_reach(m_arr, start)
  end

  @spec map_can_reach(m_arr :: %{}, start :: integer) :: boolean
  def map_can_reach(m_arr, start) do
    if start < 0 or start >= map_size(m_arr) || m_arr[start] < 0 do
      false
    else
      m_arr = Map.put(m_arr, start, m_arr[start]*-1)
      m_arr[start] == 0 or map_can_reach(m_arr, start + m_arr[start]) or map_can_reach(m_arr, start - m_arr[start])
    end
  end

  # Time Limite Exceeded. 55/56
  @spec can_reach2(arr :: [integer], start :: integer) :: boolean
  def can_reach2(arr, start) do
    if start < 0 or start >= Enum.count(arr) || Enum.at(arr, start) < 0 do
      false
    else
      arr = List.replace_at(arr, start, Enum.at(arr, start)*-1)
      Enum.at(arr, start) == 0 or can_reach2(arr, start + Enum.at(arr, start)) or can_reach2(arr, start - Enum.at(arr, start))
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    arr = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    start = Enum.at(flds, 1) |> String.to_integer()
    "arr = [" <>  Mylib.intList_to_string(arr) <> "], start = " <> Integer.to_string(start) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.can_reach(arr, start)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
