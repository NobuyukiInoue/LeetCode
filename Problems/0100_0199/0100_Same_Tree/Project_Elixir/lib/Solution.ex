defmodule Solution do
  # 325ms - 475ms
  @spec is_same_tree(p :: TreeNode.t | nil, q :: TreeNode.t | nil) :: boolean
    def is_same_tree(p, q) do
      p == q
    end

  # 297ms - 436ms
  # def is_same_tree(p, q) do
  #   cond do
  #     p == nil and q == nil ->
  #       true
  #     p == nil or q == nil ->
  #       false
  #     p.val == q.val ->
  #       if is_same_tree(p.left, q.left) do
  #         is_same_tree(p.right, q.right)
  #       else
  #         false
  #       end
  #     true ->
  #       false
  #   end
  # end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    flds = String.replace(temp, ", ", ",")
    nums = for num <- String.split(flds, "],["), do: num |> String.trim()
    p = OperateTreeNode.createTreeNode(String.split(Enum.at(nums, 0), ","))
    q = OperateTreeNode.createTreeNode(String.split(Enum.at(nums, 1), ","))
    "p = " <> OperateTreeNode.treenode_to_string(p) |> IO.puts()
    "q = " <> OperateTreeNode.treenode_to_string(q) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.is_same_tree(p, q)
      "result = " <>  to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
