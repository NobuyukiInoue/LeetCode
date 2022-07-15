defmodule Solution do
  # 288ms - 401ms
  @spec evaluate_tree(root :: TreeNode.t | nil) :: boolean
  def evaluate_tree(node) when node.val == 0, do: false
  def evaluate_tree(node) when node.val == 1, do: true
  def evaluate_tree(node) when node.val == 2, do: evaluate_tree(node.left) || evaluate_tree(node.right)
  def evaluate_tree(node), do: evaluate_tree(node.left) && evaluate_tree(node.right)

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")
    nums = for num <- String.split(flds, ","), do: num |> String.trim()
    root = OperateTreeNode.createTreeNode(nums)
    "root = " <> OperateTreeNode.treenode_to_string(root) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.evaluate_tree(root)
      "result = " <>  to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
