defmodule Mylibs do
  @spec intListToString(nums :: [integer]) :: String.t
  def intListToString(nums) do
    Enum.join(nums, ", ")
  end

  @spec intIntListToString(nums :: [[integer]]) :: String.t
  def intIntListToString(nums) do
    res =
    for arr <- nums do
      "[" <> intListToString(arr) <> "]"
    end
    Enum.join(res, ", ")
  end

  @spec matrixToString(name :: String.t, nums :: [[integer]]) :: String.t
  def matrixToString(name, nums) do
    res =
    for arr <- nums do
      " [" <> intListToString(arr) <> "]"
    end
    name <> " = [\n" <> Enum.join(res, ",\n") <> "\n]"
  end

  @spec stringArrayToString(arr :: [String]) :: String.t
  def stringArrayToString(arr) do
    "[" <> Enum.join(arr, ", ") <> "]"
  end
end
