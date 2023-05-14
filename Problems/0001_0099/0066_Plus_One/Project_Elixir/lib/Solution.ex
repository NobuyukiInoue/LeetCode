defmodule Solution do
  # 292ms - 315ms
  @spec plus_one(digits :: [integer]) :: [integer]
  def plus_one(digits) do
    res = Enum.reverse(digits)
    |>
      Enum.reduce({[], 1}, fn num, {res, carry} ->
        if num + carry < 10 do
          {[(num + carry) | res], 0}
        else
          {[0 | res], 1}
        end
      end)
    if elem(res, 1) == 1 do
      [1 | elem(res, 0)]
    else
      elem(res, 0)
    end
  end

  # 265ms - 276ms
  def plus_one2(digits) do
    digits |> Integer.undigits() |> Kernel.+(1) |> Integer.digits()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, ",")

    digits = for n <- flds, do: n |> String.trim() |> String.to_integer()
    "digits = [" <> Mylib.intList_to_string(digits) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.plus_one(digits)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
