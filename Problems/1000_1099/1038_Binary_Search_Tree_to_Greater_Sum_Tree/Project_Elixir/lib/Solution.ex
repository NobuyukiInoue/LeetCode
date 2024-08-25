defmodule Solution do
  # 221ms - 270ms
  @spec bst_to_gst(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def bst_to_gst(root) do
    reverse_inorder_traversal(0, root) |> elem(1)
  end

  @spec reverse_inorder_traversal(sum :: Integer, root :: TreeNode.t | nil) :: {Integer , TreeNode.t | nil}
  def reverse_inorder_traversal(sum, node) when node == nil do
    {sum, node}
  end

  def reverse_inorder_traversal(sum, node) do
    {sum, node_right} = reverse_inorder_traversal(sum, node.right)
    sum = sum + node.val
    node = %TreeNode{val: sum, left: node.left, right: node_right}
    {sum, node_left} = reverse_inorder_traversal(sum, node.left)
    {sum, %TreeNode{val: node.val, left: node_left, right: node_right}}
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
      result = Solution.bst_to_gst(root)
      "result = " <> OperateTreeNode.treenode_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
