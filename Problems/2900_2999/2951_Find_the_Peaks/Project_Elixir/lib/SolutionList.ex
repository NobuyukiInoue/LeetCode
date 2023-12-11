# 263ms - 351ms
defmodule SolutionList do
  @spec find_peaks(mountain :: [integer]) :: [integer]
  def find_peaks(mountain) do
    find_peaks(mountain, Enum.count(mountain))
  end

  @spec find_peaks(mountain :: [integer], n :: integer) :: [integer]
  def find_peaks(_mountain, n) when n < 3 do
    []
  end

  def find_peaks(mountain, n) do
    Enum.reduce(1..n-2, [], fn i, res ->
      if Enum.at(mountain, i - 1) < Enum.at(mountain, i) and Enum.at(mountain, i) > Enum.at(mountain, i + 1) do
        res ++ [i]
      else
        res
      end
    end)
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
