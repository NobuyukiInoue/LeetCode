defmodule Solution2 do
  # 751ms - 968ms
  @spec roman_to_int(s :: String.t) :: integer
  def roman_to_int(s) do
    roman_map = %{I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000}
    sum_romans(s, roman_map)
  end

  defp sum_romans(roman_value, roman, sum \\ 0)

  defp sum_romans("", _roman, sum), do: sum

  defp sum_romans(<<first::utf8, "">>, roman, sum) do
    first_atom_value = String.to_atom(<<first>>)

    sum = sum + roman[first_atom_value]
    sum_romans("", roman, sum)
  end

  defp sum_romans(<<first::utf8, rest::binary>>, roman, sum) do
    first_atom_value = String.to_atom(<<first>>)
    <<next::utf8, _tail::binary>> = rest
    next_atom_value = String.to_atom(<<next>>)

    if String.first(rest) && roman[first_atom_value] < roman[next_atom_value] do
      sum = sum - roman[first_atom_value]
      sum_romans(rest, roman, sum)
    else
      sum = sum + roman[first_atom_value]
      sum_romans(rest, roman, sum)
    end
  end
end
