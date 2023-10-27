defmodule Solution do
  # 285ms - 310ms
  @spec find_lu_slength(strs :: [String.t]) :: integer
  def find_lu_slength(strs) do
    len_strs = Enum.count(strs)
    Enum.reduce(0..len_strs - 1, -1, fn i, max_len ->
      count =
        Enum.reduce_while(0..len_strs - 1, 0, fn j, count ->
          if i != j do
            if not is_sub_sequence(Enum.at(strs, i), Enum.at(strs, j)) do
              {:cont, count + 1}
            else
              {:halt, count}
            end
          else
            {:cont, count}
          end
        end)
      if count == len_strs - 1 do
        max(max_len, String.length(Enum.at(strs, i)))
      else
        max_len
      end
    end)
  end

  @spec is_sub_sequence(a :: String.t, b :: String.t) :: bool
  def is_sub_sequence(a, b) do
    i =
      Enum.reduce(0..String.length(b)-1, 0, fn j, i ->
        if String.at(a, i) == String.at(b, j) do
          i + 1
        else
          i
        end
      end)
    i == String.length(a)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, ", ", ",")
    strs = String.split(temp, ",")
    "strs = " <> Mylib.stringArray_to_string(strs) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_lu_slength(strs)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
