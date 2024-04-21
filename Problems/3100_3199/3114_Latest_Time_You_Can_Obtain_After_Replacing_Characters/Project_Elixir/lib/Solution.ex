defmodule Solution do
  # 308ms - 346ms
  @spec find_latest_time(s :: String.t) :: String.t
  def find_latest_time(s) do
    map_s =
      Enum.reduce(String.to_charlist(s), {0, %{}}, fn ch, {i, map_s} ->
        {i + 1, Map.put(map_s, i, ch)}
      end)
      |> elem(1)
    map_s =
      if map_s[0] == ?? do
          if map_s[1] == ?? or map_s[1] <= ?1 do
            Map.put(map_s, 0, ?1)
          else
            Map.put(map_s, 0, ?0)
          end
      else
        map_s
      end
    map_s =
      if map_s[1] == ?? do
        if map_s[0] == ?1 do
          Map.put(map_s, 1, ?1)
        else
          Map.put(map_s, 1, ?9)
        end
      else
        map_s
    end
    map_s =
      if map_s[3] == ?? do
        Map.put(map_s, 3, ?5)
      else
        map_s
      end
    map_s =
      if map_s[4] == ?? do
        Map.put(map_s, 4, ?9)
      else
        map_s
      end
    map_s
    |> Map.values()
    |> to_string()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_latest_time(s)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
