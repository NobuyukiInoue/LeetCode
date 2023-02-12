defmodule Solution2 do
  # 431ms - 452ms
  @spec separate_digits(nums :: [integer]) :: [integer]
  def separate_digits(nums) do
    separate_digits(nums, [])
  end

  @spec separate_digits(nums :: [integer], ans :: [integer]) :: [integer]
  def separate_digits([], ans) do
    ans
  end

  def separate_digits([head | tail], ans) do
    separate_digits(tail, ans ++ str_to_arr(Integer.to_charlist(head, 10) , []))
  end

  @spec str_to_arr(strs :: [Chars], arr :: [integer]) :: [integer]
  def str_to_arr([], arr) do
    arr
  end

  def str_to_arr([head | tail], arr) do
    a1 = arr ++ [(head - ?0)]
    str_to_arr(tail, a1)
  end
end
