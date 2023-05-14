defmodule Solution2 do
  # 351ms - 361ms
  @spec deepest_leaves_sum(root :: TreeNode.t | nil) :: integer
  def deepest_leaves_sum(root) do
    [root]
    |> find_deepest_vals([])
    |> Enum.sum()
  end

  def find_deepest_vals([], vals), do: vals
  def find_deepest_vals(trees, _) do
    curr_vals = trees |> Enum.map(&(&1.val))
    next_level =
      trees
      |> Enum.flat_map(fn tree -> [tree.left, tree.right] end)
      |> Enum.reject(fn tree -> tree == nil end)

    find_deepest_vals(next_level, curr_vals)
  end
end
