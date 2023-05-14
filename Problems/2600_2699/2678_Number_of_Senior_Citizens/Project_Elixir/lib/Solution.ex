defmodule Solution do
  # 282ms - 342ms
  @spec count_seniors(details :: [String.t]) :: integer
  def count_seniors(details) do
    details |>
      Enum.reduce(0, fn detail, ans ->
        if String.to_integer(String.slice(detail, 11, 2)) > 60 do
          ans + 1
        else
          ans
        end
      end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")

    details = for fld <- String.split(flds, ",") do String.replace(fld, "\"", "") end
    "details = [" <> Mylib.stringArray_to_string(details) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_seniors(details)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
