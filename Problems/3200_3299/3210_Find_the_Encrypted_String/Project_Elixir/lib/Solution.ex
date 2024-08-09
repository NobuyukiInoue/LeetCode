defmodule Solution do
  # 353ms - 367ms
  @spec get_encrypted_string(s :: String.t, k :: integer) :: String.t
  def get_encrypted_string(s, k) do
    n = String.length(s)
    k = rem(k, n)
    if k == 0 do
      s
    else
      String.slice(s, k..n-1) <> String.slice(s, 0..k-1)
    end
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
      result = Solution.get_encrypted_string(s, k)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
