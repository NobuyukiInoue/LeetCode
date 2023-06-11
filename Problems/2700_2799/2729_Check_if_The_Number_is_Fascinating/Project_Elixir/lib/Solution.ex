defmodule Solution do
  # 279ms - 320ms
  @spec is_fascinating(n :: integer) :: boolean
  def is_fascinating(n) do
    Enum.reduce_while([n, 2*n, 3*n], {false, %{}}, fn cur, {_, cnts} ->
      {res, cnts} = temp_while(cur, cnts)
      if res do
        {:cont, {true, cnts}}
      else
        {:halt, {false, cnts}}
      end
    end) |> elem(0)
  end

  @spec temp_while(temp :: integer, cnts :: %{}) :: {boolean, %{}}
  def temp_while(temp, cnts) when temp > 0 do
    md = rem(temp, 10)
    if Map.has_key?(cnts, md) or md == 0 do
      {false, cnts}
    else
      temp_while(div(temp, 10), Map.put(cnts, md, true))
    end
  end

  def temp_while(_, cnts) do
    {true, cnts}
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")
    n = String.to_integer(flds)
    "n = " <> to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_fascinating(n)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
