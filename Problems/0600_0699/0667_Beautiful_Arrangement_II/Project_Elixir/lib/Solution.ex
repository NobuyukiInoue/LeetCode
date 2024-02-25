defmodule Solution do
  # 261ms - 286ms
  @spec construct_array(n :: integer, k :: integer) :: [integer]
  def construct_array(n, k) do
    helper(n, k, 1, n, []) |> Enum.reverse()
  end

  @spec helper(n :: integer, k :: integer, l :: integer, r :: integer, ans :: [integer]) :: [integer]
  def helper(n, k, l, r, ans) when l <= r do
    if k > 1 do
      if rem(k, 2) != 0 do
        helper(n, k - 1, l + 1, r, [l] ++ ans)
      else
        helper(n, k - 1, l, r - 1, [r] ++ ans)
      end
    else
      helper(n, k, l + 1, r, [l] ++ ans)
    end
  end

  def helper(_n, _k, _l, _r, ans) do
    ans
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    n = String.to_integer(Enum.at(flds, 0))
    k = String.to_integer(Enum.at(flds, 1))
    "n = " <> to_string(n) <> ", k = " <> to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.construct_array(n, k)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
