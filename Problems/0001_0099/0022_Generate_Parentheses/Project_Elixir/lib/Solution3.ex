defmodule Solution3 do
  # 238ms - 252ms
  @spec generate_parenthesis(n :: integer) :: [String.t]
  def generate_parenthesis(n) do
    Task.async(fn -> gen_parens(n) end)
    |> Task.await(:infinity)
    |> Enum.to_list()
  end

  defp gen_parens(0), do: []

  defp gen_parens(1), do: ["()"]

  defp gen_parens(n) do
    memoized(n, fn ->
      solutions =
        for i <- 1..n-1//1,
            j = n - i,
            front <- gen_parens(i),
            rear <- gen_parens(j),
            into: MapSet.new() do
          front <> rear
        end
      gen_parens(n-1)
      |> Stream.map(&"(#{&1})")
      |> Enum.into(solutions)
    end)
  end

  defp memoized(key, fun) do
    case Process.get(key) do
      nil ->
        value = fun.()
        Process.put(key, value)
        value
      value ->
        value
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")
    n = String.to_integer(flds)
    "n = " <> to_string(n) |> IO.puts()

    execright = Benchmark.measure(fn ->
      result = Solution.generate_parenthesis(n)
      "result = " <> Mylib.stringArray_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(execright, 3)) <> " [s]\n" |> IO.puts()
  end
end
