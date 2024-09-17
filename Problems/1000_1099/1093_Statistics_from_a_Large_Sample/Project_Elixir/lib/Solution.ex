defmodule Solution do
  # 266ms - 271ms
  @spec sample_stats(count :: [integer]) :: [float]
  def sample_stats(count) do
    {_i, v_min, v_max, n, v_sum, _v_maxcnt, mode} =
      Enum.reduce(count, {0, -1.0, -1.0, 0, 0, 0, 0.0}, fn cur, {i, v_min, v_max, n, v_sum, v_maxcnt, mode} ->
        if cur == 0 do
          {i + 1, v_min, v_max, n, v_sum, v_maxcnt, mode}
        else
          v_min =
            if v_min == -1 do
              i
            else
              v_min
            end
          {v_maxcnt, mode} =
            if cur > v_maxcnt do
              {cur, i}
            else
              {v_maxcnt, mode}
            end
          {i + 1, v_min, max(v_max, i), n + cur, v_sum + i*cur, v_maxcnt, mode}
        end
      end)
    median =
      if rem(n, 2) == 1 do
          kth(count, div(n, 2) + 1)
      else
          (kth(count, div(n, 2)) + kth(count, div(n, 2) + 1))/2
      end
    [v_min, v_max, v_sum/n, median, mode]
  end

  @spec kth(count :: [integer], k :: integer) :: integer
  def kth(count, k) do
    Enum.reduce_while(count, {0, k}, fn cur, {i, k} ->
      k = k - cur
      if k <= 0 do
        {:halt, {i, k}}
      else
        {:cont, {i + 1, k}}
      end
    end) |> elem(0)
  end

  @spec floatList_to_string(nums :: [integer]) :: String.t
  def floatList_to_string(nums) do
    Enum.join(nums, ", ")
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    count = for n <- String.split(flds, ",") do String.to_integer(n) end
    "count = [" <> floatList_to_string(count) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sample_stats(count)
      "result = " <> floatList_to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
