defmodule Solution do
  # 382ms - 402ms
  @spec is_symmetric(root :: TreeNode.t | nil) :: boolean
  def is_symmetric(root) do
    if root == nil do
      true
    else
      checkSymmetric(root.left, root.right)
    end
  end

  @spec checkSymmetric(temp1 :: TreeNode.t | nil, temp2 :: TreeNode.t | nil) :: boolean
  def checkSymmetric(temp1, temp2) do
    cond do
      temp1 == nil and temp2 == nil ->
        true
      temp1 == nil or temp2 == nil ->
        false
      temp1.val != temp2.val ->
        false
      true ->
        checkSymmetric(temp1.left, temp2.right) and checkSymmetric(temp1.right, temp2.left)
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")
    root = OperateTreeNode.createTreeNode(String.split(flds, ","))
    "root = " <> OperateTreeNode.treenode_to_string(root) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_symmetric(root)
      "result = " <>  to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
