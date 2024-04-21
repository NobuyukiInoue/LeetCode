defmodule Solution do
  # 377ms - 382ms
  @spec max_score_sightseeing_pair(values :: [integer]) :: integer
  def max_score_sightseeing_pair(values) do
    Enum.reduce(values |> tl, {1, 0, values |> hd}, fn val_i, {i, ans, prev}->
      {i + 1, max(ans, val_i - i + prev), max(prev, val_i + i)}
    end)
    |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    values = for n <- String.split(flds, ",") do String.to_integer(n) end
    "values = [" <> Mylib.intList_to_string(values) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_score_sightseeing_pair(values)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
