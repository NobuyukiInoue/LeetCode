defmodule Solution do
  # 918ms - 1075ms
  @spec count_k_constraint_substrings(s :: String.t, k :: integer) :: integer
  def count_k_constraint_substrings(s, k) do
    n = String.length(s)
    Enum.reduce(0..n-1, 0, fn i, ans ->
      Enum.reduce(i..n-1, {ans, 0, 0}, fn j, {ans, count0, count1} ->
        {count0, count1} =
          if String.at(s, j) == "0" do
            {count0 + 1, count1}
          else
            {count0, count1 + 1}
          end
        if count0 <= k or count1 <= k do
          {ans + 1, count0, count1}
        else
          {ans, count0, count1}
        end
      end) |> elem(0)
    end)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    s = String.replace(Enum.at(flds, 0), "\"", "")
    k = String.to_integer(Enum.at(flds, 1))
    "s = \"" <> s <> "\", k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.count_k_constraint_substrings(s, k)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
