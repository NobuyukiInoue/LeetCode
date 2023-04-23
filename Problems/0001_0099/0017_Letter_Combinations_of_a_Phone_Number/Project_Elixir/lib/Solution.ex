defmodule Solution do
  # 246ms - 241ms
  @spec letter_combinations(digits :: String.t) :: [String.t]
  def letter_combinations("") do
    []
  end

  def letter_combinations(digits) do
    m = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    helper(m, digits, 0, "", [])
  end

  @spec helper(m :: [String.t], digits :: String.t, pos :: integer, s :: String.t, ans :: [String.t]) :: [String.t]
  def helper(m, digits, pos, s, ans) do
    if pos == String.length(digits) do
      [s | ans]
    else
      chs = String.codepoints(Enum.at(m, String.at(digits, pos) |> String.to_integer()))
      n_ans = Enum.map(chs, fn(ch) -> helper(m, digits, pos + 1, s <> ch , ans) end)
      Enum.flat_map(n_ans, fn(x) -> x end)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    digits = String.replace(temp, ", ", ",")
    "digits = \"" <> digits <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.letter_combinations(digits)
      "result = " <> Mylib.stringArray_to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
