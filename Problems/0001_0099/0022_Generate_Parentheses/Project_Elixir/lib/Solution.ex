defmodule Solution do
  # 240ms - 263ms
  @spec generate_parenthesis(n :: integer) :: [String.t]
  def generate_parenthesis(n) do
    Enum.reverse(helper(n, 0, 0, "", []))
  end

  @spec helper(n :: integer, left :: integer, right :: integer, temp :: String.t, res :: [String.t]) :: [String.t]
  def helper(n, _, right, temp, res) when n == right do
    [temp | res]
  end

  def helper(n, left, right, temp, res) do
    if left != n do
      n_res = helper(n, left + 1, right , temp <> "(", res)
      if left > right do
        helper(n, left, right + 1 , temp <> ")", n_res)
      else
        n_res
      end
    else
      if left > right do
        helper(n, left, right + 1 , temp <> ")", res)
      else
        res
      end
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")
    n = String.to_integer(flds)
    "n = " <> to_string(n) |> IO.puts()

    execright = Benchmark.measure(fn ->
      result = Solution.generate_parenthesis(n)
      "result = " <> Mylib.stringArray_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(execright, 3)) <> " [s]\n" |> IO.puts()
  end
end
