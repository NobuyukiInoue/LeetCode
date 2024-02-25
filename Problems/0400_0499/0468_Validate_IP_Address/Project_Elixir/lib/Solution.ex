defmodule Solution do
  # 268ms - 276ms
  @spec valid_ip_address(query_ip :: String.t) :: String.t
  def valid_ip_address(query_ip) do
    flds_ipv4 = String.split(query_ip, ".")
    flds_ipv6 = String.split(query_ip, ":")
    cond do
      Enum.count(flds_ipv4) == 4 and Enum.all?(flds_ipv4, fn(s) -> is_ipv4(s) end) ->
        "IPv4"
      Enum.count(flds_ipv6) == 8 and Enum.all?(flds_ipv6, fn(s) -> is_ipv6(s) end) ->
        "IPv6"
      true ->
        "Neither"
    end
  end

  @spec is_ipv4(s :: String.t) :: Boolean
  def is_ipv4(s) do
    try do
      s_int = String.to_integer(s)
      Integer.to_string(s_int) == s and 0 <= s_int and s_int <= 255
    rescue
      _ -> false
    end
  end

  @spec is_ipv6(s :: String.t) :: Boolean
  def is_ipv6(s) do
    try do
      String.length(s) <= 4 and String.to_integer(s, 16) >= 0
    rescue
      _ -> false
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    query_ip = String.replace(temp, ", ", ",")
    "query_ip = \"" <> query_ip <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.valid_ip_address(query_ip)
      "result = \"" <> result <> "\"" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
