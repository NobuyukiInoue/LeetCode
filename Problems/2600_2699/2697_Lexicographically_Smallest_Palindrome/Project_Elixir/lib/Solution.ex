defmodule Solution do
  # 1012ms - 1029ms
  @spec make_smallest_palindrome(s :: String.t) :: String.t
  def make_smallest_palindrome(s) do
    len_s = String.length(s)
    if len_s == 1 do
      s
    else
      make_smallest_palindrome(s, len_s)
    end
  end

  @spec make_smallest_palindrome(s :: String.t, len_s :: integer) :: String.t
  def make_smallest_palindrome(s, len_s) do
    arr_s = Enum.chunk_every(String.codepoints(s), div(len_s, 2))

    arr0 = Enum.at(arr_s, 0)
    arr1 =
      if rem(len_s, 2) == 0 do
        Enum.at(arr_s, 1) |> Enum.reverse
      else
        [Enum.at(arr_s, 2) |> hd | Enum.at(arr_s, 1) |> tl |> Enum.reverse]
      end

    res = Enum.zip_reduce(arr0, arr1, {"", ""}, fn a, b, {former, latter} ->
      if a > b do
        {former <> b, b <> latter}
      else
        {former <> a, a <> latter}
      end
    end)

    if rem(len_s, 2) == 1 do
      (res |> elem(0)) <> (Enum.at(arr_s, 1) |> hd) <> (res |> elem(1))
    else
      (res |> elem(0)) <> (res |> elem(1))
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.make_smallest_palindrome(s)
      "result = \"" <> result <> "\""|> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
