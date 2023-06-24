defmodule Solution do
  # 244ms - 253ms use if
  # 274ms - 285ms use when
  @spec has_path_sum(root :: TreeNode.t | nil, target_sum :: integer) :: boolean
  def has_path_sum(root, _) when root == nil do
    false
  end

  def has_path_sum(root, target_sum) when root.left == nil and root.right == nil do
    root.val == target_sum
  end

  def has_path_sum(root, target_sum) do
    if has_path_sum(root.left, target_sum - root.val) do
      true
    else
      has_path_sum(root.right, target_sum - root.val)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")
    root = OperateTreeNode.createTreeNode(String.split(Enum.at(flds, 0), ","))
    target_sum = String.to_integer(Enum.at(flds, 1))
    "root = " <> OperateTreeNode.treenode_to_string(root) |> IO.puts()
    "target_sum = " <> Integer.to_string(target_sum) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.has_path_sum(root, target_sum)
      "result = " <>  to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
