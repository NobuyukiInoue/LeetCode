defmodule Solution do
  # 348ms - 355ms
  @spec capture_forts(forts :: [integer]) :: integer
  def capture_forts(forts) do
    forts
    |> Enum.with_index()
    |> Enum.reduce({0, 0, 0}, fn {n, i}, {j, prev, ans} ->
      cond do
        n == 0 -> {j, prev, ans}
        n == -prev -> {i, n, max(ans, i - j - 1)}
        true -> {i, n, ans}
      end
    end)
    |> elem(2)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    forts = for n <- String.split(flds, ",") do String.to_integer(n) end
    "forts = [" <> Mylib.intList_to_string(forts) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.capture_forts(forts)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
