defmodule Solution do
  # 363ms - 419ms
  @spec circular_game_losers(n :: integer, k :: integer) :: [integer]
  def circular_game_losers(n, k) do
    check = create_check_map(n, k, 1, 0, %{})
    Enum.reduce(1..n-1, [], fn i, ans ->
      cond do
        Map.get(check, i) == true ->
          ans
        i + 1 <= n ->
          [i + 1 | ans]
        true ->
          ans
      end
    end) |> Enum.reverse()
  end

  @spec create_check_map(n :: integer, k :: integer, i :: integer, pre :: integer, check :: %{}) :: %{}
  def create_check_map(n, k, i, pre, check) do
    if Map.get(check, pre) == true do
      check
    else
      create_check_map(n, k, i + 1, rem(i*k + pre, n), Map.put(check, pre, true))
    end
  end

  defp out_map(check, [head | tail]) do
    "check[" <> Integer.to_string(head) <> "] = " <> to_string(Map.get(check, head)) |> IO.puts()
    out_map(check, tail)
  end

  defp out_map(_, []) do
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    n = Enum.at(flds, 0) |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()

    "n = " <> Integer.to_string(n) <> ", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.circular_game_losers(n, k)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
