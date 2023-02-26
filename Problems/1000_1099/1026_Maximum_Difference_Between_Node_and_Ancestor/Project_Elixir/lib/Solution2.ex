defmodule Solution2 do
  # 316ms - 317ms
  @spec max_ancestor_diff(root :: TreeNode.t | nil) :: integer
  def max_ancestor_diff(root) do
    max_ancestor_diff(root, root.val, root.val, 0)
  end

  @spec max_ancestor_diff(node :: TreeNode.t | nil, v_min :: Integer, v_max :: Integer, maxDiff :: integer) :: integer
  def max_ancestor_diff(nil, _, _, maxDiff) do
    maxDiff
  end

  def max_ancestor_diff(node, v_min, v_max, maxDiff) do
    maxDiff1 = max(maxDiff, abs(v_max - node.val))
    maxDiff2 = max(maxDiff, abs(v_min - node.val))
    n_maxDiff = max(maxDiff1, maxDiff2)
    n_min = min(v_min, node.val)
    n_max = max(v_max, node.val)
    n1 = max_ancestor_diff(node.left, n_min, n_max, n_maxDiff)
    n2 = max_ancestor_diff(node.right, n_min, n_max, n_maxDiff)
    max(n1, n2)
  end
end
