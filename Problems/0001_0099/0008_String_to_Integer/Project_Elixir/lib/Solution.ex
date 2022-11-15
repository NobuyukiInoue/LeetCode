defmodule Solution do
  # 351ms - 555ms
  @spec my_atoi(s :: String.t) :: integer
  def my_atoi(s) do
    s |> String.split("", trim: true) |> preread() |> String.to_integer() |> clamp()
  end

  def preread([" " | s]), do: preread(s)
  def preread(["+" | s]), do: numread(s, "+")
  def preread(["-" | s]), do: numread(s, "-")
  def preread(s), do: numread(s, "")
  def numread([n | s], r) when n in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], do: numread(s, "#{r}#{n}")
  def numread(_, ""), do: "0"
  def numread(_, "+"), do: "0"
  def numread(_, "-"), do: "0"
  def numread(_, r), do: r

  def clamp(int) when int > 2147483647, do: 2147483647
  def clamp(int) when int < -2147483648, do: -2147483648
  def clamp(int), do: int

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    s = String.replace(temp, "\"", "")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.my_atoi(s)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
