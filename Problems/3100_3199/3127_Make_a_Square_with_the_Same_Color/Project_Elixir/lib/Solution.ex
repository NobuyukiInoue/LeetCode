defmodule Solution do
  # 313ms - 318ms
  @spec can_make_square(grid :: [[char]]) :: boolean
  def can_make_square(grid) do
    Enum.reduce_while(0..1, {false, 0}, fn i, {res, i} ->
      {res, _j} =
        Enum.reduce_while(0..1, {res, 0}, fn j, {_res, j} ->
          if is_possible(grid, i, j) do
            {:halt, {true, j + 1}}
          else
            {:cont, {false, j + 1}}
          end
        end)
      if res do
        {:halt, {true, i + 1}}
      else
        {:cont, {false, i + 1}}
      end
    end)
    |> elem(0)
  end

  @spec is_possible(grid :: [[char]], i :: integer, j :: integer) :: bool
  def is_possible(grid, i, j) do
    {cnt_w, cnt_b} =
      Enum.reduce(i..i+1, {0, 0}, fn x, {cnt_w, cnt_b} ->
        Enum.reduce(j..j+1, {cnt_w, cnt_b}, fn y, {cnt_w, cnt_b} ->
          if Enum.at(Enum.at(grid, x), y) == ?W do
            {cnt_w + 1, cnt_b}
          else
            {cnt_w, cnt_b + 1}
          end
        end)
      end)
    if cnt_w > 2 or cnt_b > 2 do
      true
    else
      false
    end
  end

  @spec charList_to_string(nums :: [char]) :: String.t
  def charList_to_string(nums) do
    Enum.join(nums, ", ")
  end

  @spec charCharList_to_string(nums :: [[char]]) :: String.t
  def charCharList_to_string(nums) do
    res =
    for arr <- nums do
      "[" <> to_string(arr)  <> "]\n"
    end
    Enum.join(res, ", ")
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, "\"", "")
    flds = String.split(temp, "],[")

    grid =
    for row <- flds do
      row |> String.replace(",", "") |> to_charlist()
    end

    "grid = [\n  " <> charCharList_to_string(grid) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.can_make_square(grid)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
