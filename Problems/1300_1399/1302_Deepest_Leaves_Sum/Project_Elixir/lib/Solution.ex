defmodule Solution do
  # 324ms - 341ms
  @spec deepest_leaves_sum(root :: TreeNode.t | nil) :: integer
  def deepest_leaves_sum(root) do
    {_, res} = deepest_leaves_sum(root, 0, 0, 0)
    res
  end

  @spec deepest_leaves_sum(node :: TreeNode.t | nil, depth :: integer, highest_depth :: integer, total :: integer) :: {integer, integer}
  def deepest_leaves_sum(nil, _, highest_depth, total) do
    {highest_depth, total}
  end

  def deepest_leaves_sum(node, depth, highest_depth, total) do
    {highest_depth, total} = deepest_leaves_sum(node.left, depth + 1, highest_depth, total)
    {highest_depth, total} = deepest_leaves_sum(node.right, depth + 1, highest_depth, total)

    if node.left == nil and node.right == nil do
      cond do
      depth > highest_depth ->
        {depth, node.val}
      depth == highest_depth ->
        {depth, total + node.val}
      true ->
        {highest_depth, total}
      end
    else
      {highest_depth, total}
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
      result = Solution.deepest_leaves_sum(root)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
