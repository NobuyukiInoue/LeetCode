defmodule Solution2 do
  @spec longest_palindrome(s :: String.t) :: String.t
  # Time Limit Exceeded.
  def longest_palindrome(s) do
    if String.length(s) < 2 do
      s
    end
    res = ""; i = 0; j = 0
    while(s, i, j, res)
  end

  @spec while(s :: String.t, i :: integer, j :: integer, res :: String.t) :: String.t
  def while(s, i, j, res) do
  # "i = " <> Integer.to_string(i) <> ", j = " <> Integer.to_string(j) |> IO.puts()
  # "arg res = " <> res |> IO.puts()
    if j < String.length(s) do
    # "isPalindrome() = " <> to_string(isPalindrome(s, i, j)) |> IO.puts()
      if isPalindrome(s, i, j) do
        if String.length(res) < (j - i + 1) do
          res = String.slice(s, i, j - i + 1)
          if i > 0 do
            while(s, i - 1, j + 1, res)
          else
            while(s, i, j + 1, res)
          end
        else
          if i > 0 do
            while(s, i - 1, j + 1, res)
          else
            while(s, i, j + 1, res)
          end
        end
      else
        while(s, i + 1, j, res)
      end
    else
      res
    end
  end

  @spec isPalindrome(s :: String.t, i :: integer, j :: integer) :: boolean
  def isPalindrome(s, i, j) do
    if i < j and String.at(s, i) == String.at(s, j) do
      isPalindrome(s, i + 1, j - 1)
    else
      !(i < j)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    s = String.replace(temp, "\"", "")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.longest_palindrome(s)
      "result = \"" <> result <> "\"" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
