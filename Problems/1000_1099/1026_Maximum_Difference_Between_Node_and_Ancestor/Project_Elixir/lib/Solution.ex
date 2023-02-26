defmodule Solution do
  # 366ms - 387ms
  @spec max_ancestor_diff(root :: TreeNode.t | nil) :: integer
  def max_ancestor_diff(root) do
    max_ancestor_diff(root, root.val, root.val)
  end

  @spec max_ancestor_diff(node :: TreeNode.t | nil, v_min :: Integer, v_max :: Integer) :: integer
  def max_ancestor_diff(nil, _, _) do
    0
  end

  def max_ancestor_diff(node, v_min, v_max) do
    n_min = min(v_min, node.val)
    n_max = max(v_max, node.val)
    max(node.val - n_min, n_max - node.val)
    |> max(max_ancestor_diff(node.left, n_min, n_max))
    |> max(max_ancestor_diff(node.right, n_min, n_max))
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")
    nums = for num <- String.split(flds, ","), do: num |> String.trim()
    root = OperateTreeNode.createTreeNode(nums)
    "root = " <> OperateTreeNode.treenode_to_string(root) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_ancestor_diff(root)
      "result = " <>  Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
