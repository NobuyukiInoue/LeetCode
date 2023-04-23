defmodule Solution do
  # 335ms - 353ms
  @spec diagonal_prime(nums :: [[integer]]) :: integer
  def diagonal_prime(nums) do
    diagonal_prime(nums, [], 0)
  end

  @spec diagonal_prime(nums :: [[integer]], diagonals :: [integer], i :: integer) :: integer
  def diagonal_prime([head | tail], diagonals, i) do
    if i != -(i + 1) do
      diagonal_prime(tail, [Enum.at(head, i) | [Enum.at(head, -(i + 1)) | diagonals]], i + 1)
    else
      diagonal_prime(tail, [Enum.at(head, i) | diagonals], i + 1)
    end
  end

  def diagonal_prime([], diagonals, _) do
    diagonals_max(diagonals |> Enum.sort(:desc))
  end

  @spec diagonals_max(diagonals :: [integer]) :: integer
  def diagonals_max([head | tail])  do
    if is_prime(head) do
      head
    else
      diagonals_max(tail)
    end
  end

  def diagonals_max([]) do
    0
  end

  @spec is_prime(n :: integer) :: bool
  def is_prime(n) do
    cond do
      n == 1 -> false
      n == 2 or n == 3 -> true
      rem(n, 2) == 0 or rem(n, 3) == 0 -> false
      true ->
        is_prime(n, trunc(:math.sqrt(n)), 5)
    end
  end

  @spec is_prime(n :: integer, limit :: integer, i :: integer) :: bool
  def is_prime(n, limit, i) when limit - i >= 0 do
    if rem(n, i) == 0 do
      false
    else
      is_prime(n, limit, i + 2)
    end
  end

  def is_prime(_, _, _) do
    true
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums =
    for fld <- flds do
      for n <- String.split(fld, ",") do
        String.to_integer(n)
      end
    end

    Mylib.matrix_to_string("nums", nums) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.diagonal_prime(nums)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
