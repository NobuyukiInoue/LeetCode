defmodule Solution do
  # 330ms - 350ms
  defmodule Solution do
    @spec separate_digits(nums :: [integer]) :: [integer]
    def separate_digits(nums) do
      nums |> Enum.flat_map(&aux/1)
    end

    def aux(n, arr \\ [])
    def aux(n, arr) when n == 0, do: arr

    def aux(n, arr) do
      aux(div(n, 10), [rem(n, 10) | arr])
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts

    exectime = Benchmark.measure(fn ->
      result = Solution.separate_digits(nums)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
