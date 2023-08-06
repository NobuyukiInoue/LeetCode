defmodule Solution do
  # 311ms - 343ms
  @spec number_of_employees_who_met_target(hours :: [integer], target :: integer) :: integer
  def number_of_employees_who_met_target(hours, target) do
    hours |>
      Enum.reduce(0, fn h, acc ->
        if h >= target, do: acc + 1, else: acc
      end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    hours = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    target = Enum.at(flds, 1) |> String.to_integer()
    "hours = [" <>  Mylib.intList_to_string(hours) <> "], target = " <> Integer.to_string(target) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.number_of_employees_who_met_target(hours, target)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
