defmodule Solution do
    # 1221ms - 1767ms
  @spec is_palindrome(x :: integer) :: boolean
  def is_palindrome(x) when x < 0, do: false
  def is_palindrome(x) when x >= 0 and x <= 9, do: true
  def is_palindrome(x) when rem(x, 10) == 0 and x != 0, do: false
  def is_palindrome(x) do
    num_tail = rem(x, 10)
    num_head = (x / 10) |> trunc()
    is_palindrome(num_head, num_tail)
  end

  @spec is_palindrome(head :: integer, tail :: integer) :: boolean
  def is_palindrome(head, _tail) when head == 0, do: false
  def is_palindrome(head, tail) when head == tail, do: true
  def is_palindrome(head, tail) when tail == (head / 10) |> trunc(), do: true
  def is_palindrome(head, tail) do
    num_tail = rem(head, 10)
    num_head = (head / 10) |> trunc()
    is_palindrome(num_head, 10 * tail + num_tail)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    x = String.to_integer(temp)
    "x = " <> Integer.to_string(x) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_palindrome(x)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
