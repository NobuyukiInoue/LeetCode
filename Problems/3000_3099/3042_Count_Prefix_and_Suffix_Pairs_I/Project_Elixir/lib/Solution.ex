defmodule Solution do
  # 305ms - 360ms
  @spec count_prefix_suffix_pairs(words :: [String.t]) :: integer
  def count_prefix_suffix_pairs(words) do
    helper(words, words |> tl, 0)
  end

  @spec helper(words1 :: [String.t], words2 :: [String.t], ans :: integer) :: integer
  def helper([_h1 | []], [], ans) do
    ans
  end

  def helper([_h1 | [t1h | t1t]], [], ans) do
    helper([t1h | t1t], t1t, ans)
  end

  def helper([h1 | t1], [h2 | t2], ans) do
    if String.starts_with?(h2, h1) and String.ends_with?(h2, h1) do
      helper([h1 | t1], t2, ans + 1)
    else
      helper([h1 | t1], t2, ans)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    words = String.split(temp, ",")
    "words = " <>  Mylib.stringArray_to_string(words) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_prefix_suffix_pairs(words)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
