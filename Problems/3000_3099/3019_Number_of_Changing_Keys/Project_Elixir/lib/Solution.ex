defmodule Solution do
  # 350ms - 367ms
  @spec count_key_changes(s :: String.t) :: integer
  def count_key_changes(s) do
    arr_s = s |> String.to_charlist()
    Enum.reduce(arr_s |> tl, {arr_s |> hd, 0}, fn ch, {prev, ans} ->
      val = abs(ch - prev)
      if val == 0 or val == 0x20 do
        {ch, ans}
      else
        {ch, ans + 1}
      end
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_key_changes(s)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
