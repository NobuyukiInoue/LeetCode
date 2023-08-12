defmodule Solution do
  # 457ms - 488ms
  @spec final_string(s :: String.t) :: String.t
  def final_string(s) do
    Enum.reduce(String.codepoints(s), "", fn ch, ans ->
      if ch == "i" do
        String.reverse(ans)
      else
        ans <> ch
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.final_string(s)
      "result = \"" <> result <> "\""|> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
