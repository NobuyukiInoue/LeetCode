defmodule Mylibs do
  def intListToString(nums) do
    "[" <> Enum.join(nums, ", ") <> "]"
  end

  def intIntListToString(nums) do
    res = []
    for arr <- nums do
        res = [intListToString(arr) | res]
    end
    Enum.reverse(res)
    "[" <> Enum.join(res, ", ") <> "]"
  end
end
