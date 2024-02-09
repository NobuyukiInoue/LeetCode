defmodule Solution do
  # 313ms - 318ms
  @spec triangle_type(nums :: [integer]) :: String.t
  def triangle_type(nums) do
    [l1 | [l2 | [l3]]] = Enum.sort(nums)
    cond do
      l1 + l2 <= l3 ->
        "none"
      l1 == l2 and l2 == l3 ->
        "equilateral"
      l1 == l2 or l2 == l3 ->
        "isosceles"
      true ->
        "scalene"
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.triangle_type(nums)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
