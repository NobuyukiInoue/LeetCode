defmodule Solution2 do
  # 240ms - 257ms
  @spec search_insert(nums :: [integer], target :: integer) :: integer
  def search_insert(nums, target) do
    search_insert(nums, target, 0)
  end

  @spec search_insert(nums :: [integer], target :: integer, idx :: integer) :: integer
  def search_insert([head | _], target, idx) when target <= head do
    idx
  end

  def search_insert([_ | tail], target, idx) do
    search_insert(tail, target, idx + 1)
  end

  def search_insert([], _, idx) do
    idx
  end
end
