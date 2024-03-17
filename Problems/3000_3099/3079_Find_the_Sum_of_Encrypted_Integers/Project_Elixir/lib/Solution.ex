defmodule Solution do
  # 295ms - 330ms
  @spec sum_of_encrypted_int(nums :: [integer]) :: integer
  def sum_of_encrypted_int(nums) do
    Enum.reduce(nums, 0, fn num, ans ->
      {m, l} = get_max_and_length(num, 0, 0)
      ans + get_total(m, l, 0)
    end)
  end

  @spec get_max_and_length(num :: integer, m :: integer, l :: integer) :: {integer, integer}
  def get_max_and_length(num, m, l) when num == 0 do
    {m, l}
  end

  def get_max_and_length(num, m, l) do
    get_max_and_length(div(num, 10), max(m, rem(num, 10)), l + 1)
  end

  @spec get_total(m :: integer, l :: integer, total :: integer) :: integer
  def get_total(_m, l, total) when l == 0 do
    total
  end

  def get_total(m, l, total) do
    get_total(m*10, l - 1, total + m)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sum_of_encrypted_int(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
