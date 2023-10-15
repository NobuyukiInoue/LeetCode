defmodule Solution do
  # 322ms - 361ms
  @spec number_of_points(nums :: [[integer]]) :: integer
  def number_of_points(nums) do
    lst =
      Enum.reduce(nums, MapSet.new([]), fn [n_start, n_end], lst ->
        Enum.reduce(n_start..n_end, lst, fn i, lst ->
          MapSet.put(lst, i)
        end)
      end)
    MapSet.size(lst)
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
      result = Solution.number_of_points(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
