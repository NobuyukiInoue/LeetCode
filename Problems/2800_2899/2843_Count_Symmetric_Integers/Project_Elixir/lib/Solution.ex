defmodule Solution do
  # 669ms - 717ms
  @spec count_symmetric_integers(low :: integer, high :: integer) :: integer
  def count_symmetric_integers(low, high) do
    Enum.reduce(low..high, 0, fn num, ans ->
      s_num = String.to_charlist(Integer.to_string(num))
      len_s = Enum.count(s_num)
      total =
        if len_s > 1 do
          Enum.reduce(0..div(len_s, 2) - 1, 0, fn i, total ->
            total + Enum.at(s_num, i) - Enum.at(s_num, len_s - i - 1)
          end)
        else
          0
        end
      if rem(len_s, 2) == 0 and total == 0 do
        ans + 1
      else
        ans
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    low = Enum.at(flds, 0) |> String.to_integer()
    high = Enum.at(flds, 1) |> String.to_integer()
    "low = " <>  Integer.to_string(low) <> ", high = " <> Integer.to_string(high) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = count_symmetric_integers(low, high)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
