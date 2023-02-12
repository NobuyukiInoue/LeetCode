defmodule Solution2 do
  # Time Limit Exceeded
  @spec longest_common_prefix(strs :: [String.t]) :: String.t
  def longest_common_prefix([]) do
    ""
  end

  def longest_common_prefix(strs) do
    longest_common_prefix(strs, Enum.at(strs, 0))
  end

  @spec longest_common_prefix(strs :: [String.t], substr :: String.t) :: String.t
  def longest_common_prefix([], substr) do
    substr
  end

  def longest_common_prefix(_, "") do
    ""
  end

  def longest_common_prefix([head | tail], substr) do
    "haed = " <> head <> ", substr = " <> substr |> IO.puts()
    "string_index(head, substr) == " <> Integer.to_string(string_index(head, substr)) |> IO.puts()
    if string_index(head, substr) == 0 do
      longest_common_prefix(tail, substr)
    else
      longest_common_prefix(tail, prefix(head, String.slice(substr, 0, String.length(substr) - 1)))
    end
  end

  @spec prefix(workstr :: String.t, substr :: String.t) :: String.t
  def prefix(_, "") do
    ""
  end

  def prefix(workstr, substr) do
    "workstr = " <> workstr <> ", substr = " <> substr |> IO.puts()
    "string_index(head, substr) == " <> Integer.to_string(string_index(workstr, substr)) |> IO.puts()
    if string_index(workstr, substr) == 0 do
      substr
    else
      prefix(workstr, String.slice(substr, 0, String.length(substr) - 1))
    end
  end

  @spec string_index(wokrstr :: String.t, substr :: String.t) :: Integer
  def string_index(workstr, substr) do
    if String.slice(workstr, 0, String.length(substr)) == substr do
      0
    else
      string_index(String.slice(workstr, 1, String.length(workstr)), substr, 0, String.length(workstr))
    end
  end

  @spec string_index(wokrstr :: String.t, substr :: String.t, index :: Integer, max_index :: integer) :: Integer
  def string_index(_, _, index, max_index) when max_index > index do
    -1
  end

  def string_index(workstr, substr, index, max_index) do
    if String.slice(workstr, 0, String.length(substr)) == substr do
      index
    else
      string_index(String.slice(workstr, 1, String.length(workstr)), substr, index + 1, max_index)
    end
  end
end
