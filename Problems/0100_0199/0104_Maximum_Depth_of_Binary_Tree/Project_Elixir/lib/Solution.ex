defmodule Solution do
  # 253ms - 302ms
  @spec max_depth(root :: TreeNode.t | nil) :: integer
  def max_depth(root) when root == nil do
    0
  end

  def max_depth(root) do
    max(max_depth(root.left), max_depth(root.right)) + 1
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")
    nums =
    if flds == "" do
      []
    else
      for num <- String.split(flds, ","), do: num |> String.trim()
    end
    root = OperateTreeNode.createTreeNode(nums)
    "root = " <> OperateTreeNode.treenode_to_string(root) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_depth(root)
      "result = " <>  Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
