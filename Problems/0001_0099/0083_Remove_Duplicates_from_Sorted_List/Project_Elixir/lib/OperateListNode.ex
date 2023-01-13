defmodule OperateListNode do
  @spec createListNode(nums :: [Integer]) :: ListNode.t | nil
  def createListNode(nums) do
    cond do
      Enum.count(nums) > 1 ->
        %ListNode{val: hd(nums), next: createListNode(tl nums)}
      Enum.count(nums) == 1 ->
        %ListNode{val: hd(nums), next: nil}
      Enum.count(nums) == 0 ->
        %ListNode{val: nil, next: nil}
    end
  end

  @spec listNodeToString(node :: nil) :: String.t
  def listNodeToString(nil) do
    ""
  end

  @spec listNodeToString(node :: ListNode.t) :: String.t
  def listNodeToString(node) do
    if node.val == nil do
      ""
    else
      if node.next != nil and node.next.val != nil do
        (node.val |> Integer.to_string()) <> ", " <> listNodeToString(node.next)
      else
        node.val |> Integer.to_string()
      end
    end
  end
end
