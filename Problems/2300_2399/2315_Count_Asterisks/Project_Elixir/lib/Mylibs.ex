defmodule Mylibs do
  def intListToString(nums) do
    "[" <> Enum.join(nums, ", ") <> "]"
  end

  def intIntListToString(nums) do
    res =
    for arr <- nums do
        intListToString(arr)
    end
    "[" <> Enum.join(res, ", ") <> "]"
  end

  def matrixToString(name, nums) do
    res =
    for arr <- nums do
        intListToString(arr)
    end
    name <> " = [\n" <> Enum.join(res, ",\n") <> "\n]"
  end
end
