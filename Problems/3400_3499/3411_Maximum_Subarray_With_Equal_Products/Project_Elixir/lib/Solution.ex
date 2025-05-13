defmodule Solution do
  # 7ms - 9ms
  @spec max_length(nums :: [integer]) :: integer
  def max_length(nums) do
    Enum.reduce_while(nums, {0, 2, nums |> tl}, fn nums_i, {i, ans, nums_tail}->
      if nums_tail == [] do
        {:halt, {i + 1, ans, []}}
      else
        {j, ans, _v_gcd, _v_lcm, is_longest} =
          Enum.reduce_while(nums_tail, {i + 1, ans, nums_i, nums_i, false}, fn nums_j, {j, ans, v_gcd, v_lcm, _is_longest} ->
            v_gcd = Integer.gcd(v_gcd, nums_j)
            if v_gcd != 1 or Integer.gcd(v_lcm, nums_j) != 1 do
              {:halt, {j + 1, max(ans, j - i), v_gcd, v_lcm, true}}
            else
              {:cont, {j + 1, ans, v_gcd, v_lcm*nums_j, false}}
            end
          end)
        if not is_longest do
          {:cont, {i + 1, max(ans, j - i), nums_tail |> tl}}
        else
          {:cont, {i + 1, ans, nums_tail |> tl}}
        end
      end
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    "nums = [" <> Mylib.intList_to_string(nums) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_length(nums)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
