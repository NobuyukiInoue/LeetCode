defmodule Solution do
  # 966ms - 1138ms
  @spec roman_to_int(s :: String.t) :: integer
  def roman_to_int(s) do
    map = %{
      "I" => 1,
      "V" => 5,
      "X" => 10,
      "L" => 50,
      "C" => 100,
      "D" => 500,
      "M" => 1000
    }
    arr = [Map.get(map, String.at(s, String.length(s) - 1))] ++
    for i <- (String.length(s) - 2)..0 do
      if Map.get(map, String.at(s, i)) >= Map.get(map, String.at(s, i + 1)) do
        Map.get(map, String.at(s, i))
      else
        -Map.get(map, String.at(s, i))
      end
    end
    Enum.sum(arr)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    s = String.replace(temp, "\"", "")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.roman_to_int(s)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
