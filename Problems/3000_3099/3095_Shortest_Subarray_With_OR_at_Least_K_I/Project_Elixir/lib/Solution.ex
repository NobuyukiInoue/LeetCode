defmodule Solution do
  # 428ms - 435ms
  @spec minimum_subarray_length(nums :: [integer], k :: integer) :: integer
  def minimum_subarray_length(nums, k) do
    m_nums =
      Enum.reduce(nums, {0, %{}}, fn num, {i, m_nums} ->
        {i + 1, Map.put(m_nums, i, num)}
      end)
      |> elem(1)
    n = Enum.count(nums)
    res =
      Enum.reduce(0..n-1, 51, fn i, res ->
        Enum.reduce(i..n-1, res, fn j, res ->
          bitwise =
            Enum.reduce(i..j, 0, fn p, bitwise ->
              Bitwise.bor(bitwise, m_nums[p])
            end)
          if bitwise >= k do
            min(res, j - i + 1)
          else
            res
          end
        end)
      end)
    if res == 51 do
      -1
    else
      res
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums =
      for num <- String.split(Enum.at(flds, 0), ",") do
          String.to_integer(num)
      end

    k = String.to_integer(Enum.at(flds, 1))

    "nums = " <> Mylib.intList_to_string(nums) <> ", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.minimum_subarray_length(nums, k)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
