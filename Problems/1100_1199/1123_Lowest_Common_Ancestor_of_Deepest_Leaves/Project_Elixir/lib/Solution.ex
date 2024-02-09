defmodule Solution do
  # 300ms
  @spec lca_deepest_leaves(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def lca_deepest_leaves(root) do
    get_deepest_node(root, 0) |> elem(1)
  end

  @spec get_deepest_node(node :: TreeNode.t | nil, depth :: Integer) :: {Integer, TreeNode.t | nil}
  def get_deepest_node(node, _depth) when node == nil do
    {0, nil}
  end

  def get_deepest_node(node, depth) do
    {l_depth, l_node} = get_deepest_node(node.left, depth + 1)
    {r_depth, r_node} = get_deepest_node(node.right, depth + 1)
    cond do
      l_depth > r_depth -> {l_depth + 1, l_node}
      l_depth < r_depth -> {r_depth + 1, r_node}
      true -> {l_depth + 1, node}
    end
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
      result = Solution.lca_deepest_leaves(root)
      "result = " <> OperateTreeNode.treenode_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
