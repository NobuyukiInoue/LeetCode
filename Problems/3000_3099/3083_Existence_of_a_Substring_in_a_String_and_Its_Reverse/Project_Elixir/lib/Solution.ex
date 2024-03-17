defmodule Solution do
  # 295ms - 319ms
  @spec is_substring_present(s :: String.t) :: boolean
  def is_substring_present(s) do
    is_substring(s, String.reverse(s))
  end

  @spec is_substring(s :: String.t, r_s :: String.t) :: boolean
  def is_substring(s, r_s) do
    l = String.length(r_s)
    cond do
      l <= 1 ->
        false
      String.contains?(s, String.slice(r_s, 0, 2)) ->
        true
      true ->
        is_substring(s, String.slice(r_s, 1..l))
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_substring_present(s)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
