defmodule Solution3 do
  # 255ms - 261ms
  @spec plus_one(digits :: [integer]) :: [integer]
  def plus_one(digits) do
    digits
    |> Enum.reverse()
    |> do_plus_one([], 1)
  end

  @spec do_plus_one(digits :: [integer], sum :: [integer], carry :: 0 | 1) :: [integer]
  defp do_plus_one([], sum, 0), do: sum
  defp do_plus_one([], sum, 1), do: [1 | sum]
  defp do_plus_one([9 | tail], sum, 1), do: do_plus_one(tail, [0 | sum], 1)
  defp do_plus_one([n | tail], sum, carry), do: do_plus_one(tail, [n + carry | sum], 0)
end
