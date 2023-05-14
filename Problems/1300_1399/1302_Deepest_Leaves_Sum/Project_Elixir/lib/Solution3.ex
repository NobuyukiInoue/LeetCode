defmodule Solution3 do
  # 359ms - 401ms
  @spec deepest_leaves_sum(root :: TreeNode.t | nil) :: integer
  def deepest_leaves_sum(root) do
    root
    |> deepest_leaves_sum(0, %{})
    |> Enum.max()
    |> elem(1)
  end

  defp deepest_leaves_sum(nil, _level, sums) do
    sums
  end

  defp deepest_leaves_sum(node, level, sums) do
    sums = Map.update(sums, level, node.val, & &1 + node.val)
    sums = deepest_leaves_sum(node.left, level + 1, sums)
    deepest_leaves_sum(node.right, level + 1, sums)
  end
end
