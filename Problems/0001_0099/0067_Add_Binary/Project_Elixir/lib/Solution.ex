defmodule Solution do
  @base 2
  # 287ms - 326ms
  @spec add_binary(a :: String.t, b :: String.t) :: String.t
  def add_binary(a, b) do
    {a, _} = Integer.parse(a, @base)
    {b, _} = Integer.parse(b, @base)
    Integer.to_string((a + b), @base)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, "],[")
    a = Enum.at(flds, 0)
    b = Enum.at(flds, 1)
    "a = \"" <> a <> "\"" <> ", b = " <> b <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.add_binary(a, b)
      "result = \"" <> result <> "\"" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
