defmodule Solution do
  # 291ms - 665ms
  @spec number_game(nums :: [integer]) :: [integer]
  def number_game(nums) do
    helper(Enum.sort(nums), [])
  end

  @spec helper(nums :: [integer], arr :: [integer]) :: [integer]
  def helper([], arr) do
    arr
  end

  def helper([h1 | [h2 | t2]], arr) do
    [h2] ++ [h1] ++ helper(t2, arr)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.number_game(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
