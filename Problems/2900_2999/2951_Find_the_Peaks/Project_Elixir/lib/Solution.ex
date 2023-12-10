defmodule Solution do
  # 285ms - 295ms
  @spec find_peaks(mountain :: [integer]) :: [integer]
  def find_peaks(mountain) do
    n = Enum.count(mountain)
    cond do
      n - 2 == 1 ->
        if Enum.at(mountain, 0) < Enum.at(mountain, 1) and Enum.at(mountain, 1) > Enum.at(mountain, 2) do
          [1]
        else
          []
        end
      n - 2 < 1 ->
        []
      true ->
        Enum.reduce(1..n-2, [], fn i, res ->
        if Enum.at(mountain, i - 1) < Enum.at(mountain, i) and Enum.at(mountain, i) > Enum.at(mountain, i + 1) do
          res ++ [i]
        else
          res
        end
      end)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    mountain = for n <- String.split(flds, ",") do String.to_integer(n) end
    "mountain = [" <> Mylib.intList_to_string(mountain) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_peaks(mountain)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
