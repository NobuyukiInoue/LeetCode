defmodule Solution do
  # 337ms - 343ms
  @spec find_k_or(nums :: [integer], k :: integer) :: integer
  def find_k_or(nums, k) do
    Enum.reduce(0..30, 0, fn i, ans ->
      rep = Bitwise.<<<(1, i)
      cnt =
        Enum.reduce(nums, 0, fn num, cnt ->
          if Bitwise.band(rep, num) != 0 do
            cnt + 1
          else
            cnt
          end
        end)
      if cnt >= k do
        ans + rep
      else
        ans
      end
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()
    "nums = [" <>  Mylib.intList_to_string(nums) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_k_or(nums, k)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
