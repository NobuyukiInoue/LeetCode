defmodule Solution do
  # 279ms - 312ms
  @spec check_arithmetic_subarrays(nums :: [integer], l :: [integer], r :: [integer]) :: [boolean]
  def check_arithmetic_subarrays(nums, l, r) do
    Enum.zip_reduce(l, r, [], fn i, j, ans ->
      res = check_diff(Enum.sort(Enum.slice(nums, i..j)))
      ans ++ [res]
    end)
  end

  @spec check_diff(temp :: [integer]) :: boolean
  def check_diff(temp) do
    if Enum.count(temp) <= 2 do
      true
    else
      [head | tail] = temp
      diff = (tail |> hd) - head
      check_diff(tail, diff)
    end
  end

  @spec check_diff(temp :: [integer], diff :: integer) :: boolean
  def check_diff([], _diff) do
    true
  end

  def check_diff([_head | tail], _diff) when tail == [] do
    true
  end

  def check_diff([head | tail], diff) do
    if (tail |> hd) - head != diff do
      false
    else
      check_diff(tail, diff)
    end
  end

  @spec boolList_to_string(arr :: [integer]) :: String.t
  def boolList_to_string(arr) do
    Enum.reduce(arr, {0, ""}, fn cur, {i, res} ->
      if i == 0 do
        {i + 1, to_string(cur)}
      else
        {i + 1, res <> ", " <> to_string(cur)}
      end
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums = for n <- String.split(Enum.at(flds, 0), ","), do: String.to_integer(n)
    l = for n <- String.split(Enum.at(flds, 1), ","), do: String.to_integer(n)
    r = for n <- String.split(Enum.at(flds, 2), ","), do: String.to_integer(n)

    "nums = [" <> Mylib.intList_to_string(nums) <> "], l = [" <> Mylib.intList_to_string(l) <> "], r = [" <> Mylib.intList_to_string(r) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.check_arithmetic_subarrays(nums, l, r)
      "result = [" <> boolList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
