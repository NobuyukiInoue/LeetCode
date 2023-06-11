defmodule Solution do
  # 410ms - 432ms
  @spec min_length(s :: String.t) :: integer
  def min_length(s) do
    cond do
      String.contains?(s, "AB") ->
        min_length(String.replace(s, "AB", ""))
      String.contains?(s, "CD") ->
        min_length(String.replace(s, "CD", ""))
      true ->
        String.length(s)
    end
  end

  # 851ms - 891ms
  @spec min_length2(s :: String.t) :: integer
  def min_length2(s) do
    n = String.length(s)
    if n <= 1 do
      n
    else
      st = Enum.reduce(1..n - 1, String.first(s), fn i, st ->
        st_hd = String.first(st)
        if String.length(st) > 0 and ((String.at(s, i) == "B" and st_hd == "A") or (String.at(s, i) == "D" and st_hd == "C")) do
          String.slice(st, 1..-1)
        else
          String.at(s, i) <> st
        end
      end)
      String.length(st)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = " <> s |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.min_length(s)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
