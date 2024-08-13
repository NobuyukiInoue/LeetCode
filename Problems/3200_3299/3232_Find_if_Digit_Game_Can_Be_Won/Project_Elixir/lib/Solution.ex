defmodule Solution do
  # 336s - 350ms
  @spec can_alice_win(nums :: [integer]) :: boolean
  def can_alice_win(nums) do
    {s_digits, d_digits} =
      Enum.reduce(nums, {0, 0}, fn num, {s_digits, d_digits} ->
        cond do
          num < 10 ->
            {s_digits + num, d_digits}
          num < 100 ->
            {s_digits, d_digits + num}
        end
      end)
      if s_digits == d_digits do
        false
      else
        true
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
      result = Solution.can_alice_win(nums)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
