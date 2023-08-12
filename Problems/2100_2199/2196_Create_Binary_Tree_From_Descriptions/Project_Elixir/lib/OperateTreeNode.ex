defmodule OperateTreeNode do
  @spec createTreeNode(nums :: [String.t]) :: TreeNode.t | nil
  def createTreeNode(nums) do
    createTreeNode(nums, 0, 0)
  end

# @spec createTreeNode(nums :: [String.t], depth :: Integer, pos :: Integer) :: TreeNode.t | nil
  def createTreeNode(nums, depth, pos) do
    cond do
      pos >= Enum.count(nums) ->
        nil
      Enum.count(nums) <= 0 ->
        nil
      true ->
        cur_pos = get_cur_pos(depth, 0)
        if (cur_pos + pos) > (Enum.count(nums) - 1) do
          nil
        else
          if Enum.at(nums, cur_pos + pos) == "null" do
            nil
          else
            %TreeNode{val: String.to_integer(Enum.at(nums, cur_pos + pos)), left: createTreeNode(nums, depth + 1, 2*pos), right: createTreeNode(nums, depth + 1, 2*pos + 1)}
          end
        end
    end
  end

  @spec get_cur_pos(depth :: Integer, i :: Integer) :: Integer
  def get_cur_pos(depth, i) do
    if i < depth do
      (:math.pow(2, i) |> round) + get_cur_pos(depth, i + 1)
    else
      0
    end
  end

  @spec treenode_to_string(node :: TreeNode.t | nil) :: String.t
  def treenode_to_string(node) do
    cond do
      node == nil ->
        ""
      node.left != nil and node.right != nil ->
        Integer.to_string(node.val) <> "(" <> treenode_to_string(node.left) <> ")(" <> treenode_to_string(node.right) <> ")"
      node.left != nil ->
        Integer.to_string(node.val) <> "(" <> treenode_to_string(node.left) <> ")()"
      node.right != nil ->
        Integer.to_string(node.val) <> "()(" <> treenode_to_string(node.right) <> ")"
      true ->
        Integer.to_string(node.val)
    end
  end

  @spec treenode_to_string2(node :: TreeNode.t | nil) :: String.t
  def treenode_to_string2(node) do
    if node == nil do
      ""
    else
      if node.left != nil and node.right != nil do
        Integer.to_string(node.val) <> "(" <> treenode_to_string(node.left) <> ")(" <> treenode_to_string(node.right) <> ")"
      else
        if node.left != nil do
          Integer.to_string(node.val) <> "(" <> treenode_to_string(node.left) <> ")()"
        else
          if node.right != nil do
            Integer.to_string(node.val) <> "()(" <> treenode_to_string(node.right) <> ")"
          else
            Integer.to_string(node.val)
          end
        end
      end
    end
  end
end
