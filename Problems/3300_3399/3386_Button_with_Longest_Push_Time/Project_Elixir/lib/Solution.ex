defmodule Solution do
  # 0ms
  @spec button_with_longest_time(events :: [[integer]]) :: integer
  def button_with_longest_time(events) do
    [ans, p_time] = events |> hd
    Enum.reduce(events, {ans, p_time, p_time}, fn [pusher, c_time], {ans, p_time, mx} ->
      diff = c_time - p_time
      {mx, ans} =
        cond do
          diff > mx ->
            {diff, pusher}
          diff == mx and pusher < ans ->
            {mx, pusher}
          true ->
            {mx, ans}
        end
      {ans, c_time, mx}
    end) |> elem(0)
  end

  @spec print_map(m_cur :: %{}) :: None
  def print_map(m_cur) do
    res =
    for key <- Map.keys(m_cur) do
      m_cur[key]
    end
    "m_keys = {" <> Enum.join(res, ", ") <> "}" |> IO.puts()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    flds = String.split(temp, "],[")

    events =
    for row <- flds do
      for col <- String.split(row, ",") do
        String.to_integer(col)
      end
    end

    "events = [" <> Mylib.intIntList_to_string(events) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.button_with_longest_time(events)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
