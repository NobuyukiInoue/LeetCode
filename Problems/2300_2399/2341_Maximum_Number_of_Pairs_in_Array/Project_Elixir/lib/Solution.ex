defmodule Solution do
  # 347ms - 408ms
  @spec number_of_pairs(nums :: [integer]) :: [integer]
  def number_of_pairs(nums) do
    nums
    |> Enum.reduce(%{}, fn n, acc ->
      Map.update(acc, n, 1, &(&1 + 1))
    end)
    |> Enum.reduce([0, 0], fn {_, v}, [a, b] ->
      [a + div(v, 2), b + rem(v, 2)]
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "numst = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.number_of_pairs(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
