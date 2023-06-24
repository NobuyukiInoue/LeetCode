defmodule Solution do
  # 1110ms - 1129ms
  @spec distance_traveled(main_tank :: integer, additional_tank :: integer) :: integer
  def distance_traveled(main_tank, additional_tank) do
    (main_tank + min(div(main_tank-1, 4), additional_tank))*10
  end

  # 1106ms - 1197ms
  @spec distance_traveled2(main_tank :: integer, additional_tank :: integer) :: integer
  def distance_traveled2(main_tank, additional_tank) do
    {ans, main_tank} = distance_traveled_while(main_tank, additional_tank, 0)
    ans + main_tank*10
  end

  @spec distance_traveled_while(main_tank :: integer, additional_tank :: integer, ans :: integer) :: {integer, integer}
  def distance_traveled_while(main_tank, additional_tank, ans) when main_tank >= 5 do
    if additional_tank >= 1 do
        distance_traveled_while(main_tank - 5 + 1, additional_tank - 1, ans + 50)
    else
      distance_traveled_while(main_tank - 5, additional_tank, ans + 50)
    end
  end

  def distance_traveled_while(main_tank, _, ans) do
    {ans, main_tank}
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    main_tank = Enum.at(flds, 0) |> String.to_integer()
    additional_tank = Enum.at(flds, 1) |> String.to_integer()
    "main_tank = " <> Integer.to_string(main_tank) <> ", additional_tank = " <> Integer.to_string(additional_tank) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.distance_traveled(main_tank, additional_tank)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
