defmodule Solution do
  # 1498ms - 2637ms
  @spec convert(s :: String.t, num_rows :: integer) :: String.t
  def convert(s, 1) do
    s
  end

  def convert(s, num_rows) do
    rows = for _i <- 0..num_rows-1 do
      []
    end
    zigzag(String.split(s, "", trim: true), rows, num_rows)
  end

  @spec zigzag(s :: [], rows :: [[]], num_rows :: integer, curr_row :: integer, direction :: integer) :: Srring.t
  defp zigzag(s, rows, num_rows, curr_row \\ 0, direction \\ 1)

  defp zigzag([], rows, _num_rows, _curr_row, _direction) do
    rows
    |> Enum.map(&Enum.reverse/1)
    |> Enum.map(&List.to_string/1)
    |> List.to_string
  end

  defp zigzag([head|tail], rows, num_rows, curr_row, direction) do
    prepended_rows = for {row, i} <- Enum.with_index(rows) do
      if i == curr_row do
        [head] ++ row
      else
        row
      end
    end
    d = cond do
      curr_row + direction == num_rows -> -1
      curr_row + direction == -1 -> 1
      true -> direction
    end
    zigzag(tail, prepended_rows, num_rows, curr_row + d, d)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, ",")
    s = Enum.at(flds, 0)
    num_rows = Enum.at(flds, 1) |> String.to_integer()
    "s = \"" <> s <> "\"" <> ", num_rows = " <> Integer.to_string(num_rows) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.convert(s, num_rows)
      "result = \"" <> result <> "\""|> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
