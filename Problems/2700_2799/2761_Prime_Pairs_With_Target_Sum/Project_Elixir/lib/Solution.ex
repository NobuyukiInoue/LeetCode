defmodule Solution do
  # Time Limit Exceeded 500 / 554
  # n = 99999, 2.078[s]
  @spec find_prime_pairs(n :: integer) :: [[integer]]
  def find_prime_pairs(n) do
    lst =
      1..n |>
      Enum.reduce(%{}, fn i, lst ->
        Map.put(lst, i, false)
      end)

    lst =
      if trunc(:math.sqrt(n)) >= 2 do
        Enum.reduce(2..trunc(:math.sqrt(n))+1, lst, fn i, lst ->
          if lst[i] != nil do
            Enum.filter(i*2..n-1, fn(x) -> rem(x, i) == 0 end) |>
            Enum.reduce(lst, fn j, lst ->
              Map.delete(lst, j)
            end)
          else
            lst
          end
        end)
      else
        lst
      end

    if div(n, 2) >= 2 do
      Enum.reduce(2..div(n, 2), [], fn i, ans ->
        x = i
        y = n - i
        if lst[x] != nil and lst[y] != nil and x <= y do
          [[x, y]] ++ ans
        else
          ans
        end
      end) |> Enum.reverse()
    else
      []
    end
  end

  # Time Limit Exceeded 500 / 554
  # n = 99999, 2.514[s]
  @spec find_prime_pairs2(n :: integer) :: [[integer]]
  def find_prime_pairs2(n) do
    lst =
      1..n |>
      Enum.reduce(%{}, fn i, lst ->
        Map.put(lst, i, false)
      end)

    lst =
      if trunc(:math.sqrt(n)) >= 2 do
        Enum.reduce(2..trunc(:math.sqrt(n))+1, lst, fn i, lst ->
          if not lst[i] do
            Enum.filter(i*2..n-1, fn(x) -> rem(x, i) == 0 end) |>
            Enum.reduce(lst, fn j, lst ->
              Map.put(lst, j, true)
            end)
          else
            lst
          end
        end)
      else
        lst
      end

    if div(n, 2) >= 2 do
      Enum.reduce(2..div(n, 2), [], fn i, ans ->
        x = i
        y = n - i
        if (not lst[x]) and (not lst[y]) and x <= y do
          [[x, y]] ++ ans
        else
          ans
        end
      end) |> Enum.reverse()
    else
      []
    end
  end

  # Time Limit Exceeded 499 / 554
  # n = 99999, 8.385[s]
  @spec find_prime_pairs3(n :: integer) :: [[integer]]
  def find_prime_pairs3(n) do
    lst =
      2..trunc(:math.sqrt(n))+1 |>
      Enum.reduce(%{}, fn i, lst ->
        Enum.filter(i*2..n-1, fn(x) -> rem(x, i) == 0 end) |>
        Enum.reduce(lst, fn j, lst -> Map.put(lst, j, true) end)
      end)

    if div(n, 2) >= 2 do
      Enum.reduce(2..div(n, 2), [], fn i, ans ->
        x = i
        y = n - i
        if lst[x] == nil and lst[y] == nil and x <= y do
          [[x, y]] ++ ans
        else
          ans
        end
      end) |> Enum.reverse()
    else
      []
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")
    n = String.to_integer(flds)
    "n = " <> to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_prime_pairs(n)
      "result = [" <> Mylib.intIntList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
