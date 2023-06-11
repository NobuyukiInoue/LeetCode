defmodule Solution2 do
  # Time Limit Exceeded 55/59
  @spec kth_smallest_prime_fraction(arr :: [integer], k :: integer) :: [integer]
  def kth_smallest_prime_fraction(arr, k) do
    len_arr = Enum.count(arr)
    if len_arr <= 2 do
      [Enum.at(arr, 0), Enum.at(arr, 1)]
    else
      res = get_current(arr, [], Enum.count(arr))
      res = Enum.sort_by(res, fn %{val: val} -> val end)
      Enum.at(res, k - 1)[:data]
    end
  end

  @spec get_current(arr :: [integer], res :: [%{}], count :: integer) :: [%{}]
  def get_current([one | least_arr], res, count) when count > 1 do
    cur =
    Enum.map(least_arr, fn two ->
      "[one, two] = " <> Integer.to_string(one) <> ", " <> Integer.to_string(two) |> IO.puts()
      %{data: [one, two], val: one/two}
    end)
    get_current(least_arr, cur ++ res, count - 1)
  end

  def get_current(_, res, _) do
    res
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    arr = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()
    "arr = [" <>  Mylib.intList_to_string(arr) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution2.kth_smallest_prime_fraction(arr, k)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
