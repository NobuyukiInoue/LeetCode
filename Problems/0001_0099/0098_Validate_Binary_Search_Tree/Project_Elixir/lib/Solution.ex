defmodule Solution do
  # 300ms - 404ms
  @spec is_valid_bst(root :: TreeNode.t | nil) :: boolean
  @spec is_valid_bst(root :: TreeNode.t | nil, m_min :: Integer, m_max :: Integer) :: boolean
  def is_valid_bst(root, m_min \\ (:math.pow(2, 31) |> round), m_max \\ -(:math.pow(2, 31) |> round) - 1) do
    cond do
      root == nil ->
        true
      root.val <= m_max or root.val >= m_min ->
        false
      true ->
        is_valid_bst(root.left, min(root.val, m_min), m_max) and is_valid_bst(root.right, m_min, max(root.val, m_max))
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
      result = Solution.is_valid_bst(root)
      "result = " <> to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
