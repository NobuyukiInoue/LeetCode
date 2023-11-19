defmodule Solution do
  # 447ms - 472ms
  @spec find_minimum_operations(s1 :: String.t, s2 :: String.t, s3 :: String.t) :: integer
  def find_minimum_operations(s1, s2, s3) do
    min_length = min(min(String.length(s1), String.length(s2)), String.length(s3))
    total_length = String.length(s1) + String.length(s2) + String.length(s3)
    if String.at(s1, 0) != String.at(s2, 0) or String.at(s2, 0) != String.at(s3, 0) or String.at(s3, 0) != String.at(s1, 0) do
      -1
    else
      Enum.zip([String.to_charlist(s1), String.to_charlist(s2), String.to_charlist(s3)]) |>
        Enum.reduce_while({0, total_length}, fn {ch1, ch2, ch3}, {i, total_length} ->
          cond do
            i >= min_length ->
              {:halt, {i + 1, total_length}}
            ch1 == ch2 and ch2 == ch3 and ch3 == ch1 ->
              {:cont, {i + 1, total_length - 3}}
            true ->
              {:halt, {i + 1, total_length}}
          end
        end) |> elem(1)
    end
  end

  # 791ms - 825ms
  @spec find_minimum_operations2(s1 :: String.t, s2 :: String.t, s3 :: String.t) :: integer
  def find_minimum_operations2(s1, s2, s3) do
    min_length = min(min(String.length(s1), String.length(s2)), String.length(s3))
    total_length = String.length(s1) + String.length(s2) + String.length(s3)
    if String.at(s1, 0) != String.at(s2, 0) or String.at(s2, 0) != String.at(s3, 0) or String.at(s3, 0) != String.at(s1, 0) do
      -1
    else
      Enum.reduce_while(0..min_length - 1, total_length, fn i, total_length ->
        if String.at(s1, i) == String.at(s2,  i) and String.at(s2,  i) == String.at(s3,  i) and String.at(s3,  i) == String.at(s1, i) do
          {:cont, total_length - 3}
        else
          {:halt, total_length}
        end
      end)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, ",")

    s1 = Enum.at(flds, 0)
    s2 = Enum.at(flds, 1)
    s3 = Enum.at(flds, 2)
    "s1 = " <>  s1 <> ", s2 = " <> s2 <> ", s3 = " <> s3 |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_minimum_operations(s1, s2, s3)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
