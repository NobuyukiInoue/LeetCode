defmodule Solution do
  # 695ms - 730ms
  @spec kth_smallest_prime_fraction(arr :: [integer], k :: integer) :: [integer]
  def kth_smallest_prime_fraction(arr, k) do
    kth_smallest_prime_fraction(arr, k, 0.0, 1.0)
  end

  def kth_smallest_prime_fraction(arr, k, lo, hi) when lo < hi do
    mid = (lo + hi)/2.0
    {_, count, best} =
      Enum.reduce(1..Enum.count(arr)-1, {0, 0, [0, 1]}, fn right, {left, count, best} ->
        left = get_next_left(arr, left, right, mid)
        count = count + left
        if left > 0 and Enum.at(best, 0)*Enum.at(arr, right) < Enum.at(best, 1)*Enum.at(arr, left - 1) do
          {left, count, [Enum.at(arr, left - 1), Enum.at(arr, right)]}
        else
          {left, count, best}
        end
      end)
    cond do
      count == k ->
        best
      count > k ->
        kth_smallest_prime_fraction(arr, k, lo, mid)
      true ->
        kth_smallest_prime_fraction(arr, k, mid, hi)
    end
  end

  def kth_smallest_prime_fraction(_, _, _, _) do
    [0, 0]
  end

  @spec get_next_left(arr :: [integer], left :: integer, right :: integer, mid :: float) :: integer
  def get_next_left(arr, left, right, mid) do
    if Enum.at(arr, left) < mid*Enum.at(arr, right) do
      get_next_left(arr, left + 1, right, mid)
    else
      left
    end
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
      result = Solution.kth_smallest_prime_fraction(arr, k)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
