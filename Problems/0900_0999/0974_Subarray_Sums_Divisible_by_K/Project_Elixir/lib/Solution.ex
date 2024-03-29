defmodule Solution do
  # 376ms - 451ms
  @spec subarrays_div_by_k(nums :: [integer], k :: integer) :: integer
  def subarrays_div_by_k(nums, k) do
    {_, mod} =
      Enum.reduce(nums, {0, %{0 => 1}}, fn num, {running_mod, mod} ->
        running_mod = get_mod(rem(num + running_mod, k), k)
        {running_mod, Map.put(mod, running_mod, Map.get(mod, running_mod, 0) + 1)}
      end)
    Enum.reduce(Map.values(mod), 0, fn m, ans ->
      ans + div(m*(m - 1),2)
    end)
  end

  @spec get_mod(running_mod :: integer, k :: integer) :: integer
  def get_mod(running_mod, k) when running_mod < 0 do
    running_mod + k
  end

  def get_mod(running_mod, _k) do
    running_mod
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

    "nums = [" <> Mylib.intList_to_string(nums) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.subarrays_div_by_k(nums, k)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
