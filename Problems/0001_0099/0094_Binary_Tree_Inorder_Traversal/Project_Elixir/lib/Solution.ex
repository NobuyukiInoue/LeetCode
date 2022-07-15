defmodule Solution do
  # 365ms - 402ms
  @spec inorder_traversal(root :: TreeNode.t | nil) :: [integer]
  def inorder_traversal(%TreeNode{val: val, left: left, right: right}) do
    inorder_traversal(left) ++ [val] ++ inorder_traversal(right)
  end

  def inorder_traversal(nil) do
    []
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
      result = Solution.inorder_traversal(root)
      "result = [" <>  Mylib.intList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
