defmodule Solution do
  # 263ms - 307ms
  @spec split_list_to_parts(head :: ListNode.t | nil, k :: integer) :: [ListNode.t | nil]
  def split_list_to_parts(head, k) do
    leng = get_listnode_length(head)
    part_size = div(leng, k)
    extra = rem(leng, k)
    split_list_to_parts(head, k, part_size, extra)
  end

  def split_list_to_parts(node, k, part_size, extra) do
    {current_part_size, extra} =
      if extra > 0 do
        {part_size + 1, extra - 1}
      else
        {part_size, extra}
      end
    if k == 1 do
      [get_listnode_any(node, current_part_size)]
    else
      node_next = get_listnode_any_next(node, current_part_size)
      [get_listnode_any(node, current_part_size)] ++ split_list_to_parts(node_next, k - 1, part_size, extra)
    end
  end

  @spec get_listnode_length(node :: ListNode.t) :: Integer
  def get_listnode_length(node) do
    get_listnode_length(node, 0)
  end

  @spec get_listnode_length(node :: ListNode.t, length :: integer) :: Integer
  def get_listnode_length(node, length) when node == nil do
    length
  end

  def get_listnode_length(node, length) do
    get_listnode_length(node.next, length + 1)
  end

  @spec get_listnode_any_next(node :: ListNode, cnt :: Integer) :: ListNode.t | nil
  def get_listnode_any_next(nil, _cnt) do
    nil
  end

  def get_listnode_any_next(node, cnt) when cnt == 1 do
    node.next
  end

  def get_listnode_any_next(node, cnt) do
    get_listnode_any_next(node.next, cnt - 1)
  end

  @spec get_listnode_any(node :: ListNode, cnt :: Integer) :: ListNode.t | nil
  def get_listnode_any(nil, _cnt) do
    nil
  end

  def get_listnode_any(_node, cnt) when cnt == 0 do
    nil
  end

  def get_listnode_any(node, cnt) do
    %ListNode{val: node.val, next: get_listnode_any(node.next, cnt - 1)}
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    nums0 = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    head = OperateListNode.createListNode(nums0)
    k = String.to_integer(Enum.at(flds, 1))
    "head = [" <> OperateListNode.listNodeToString(head) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.split_list_to_parts(head, k)

      result_strs =
        for res <- result do
          "[" <> OperateListNode.listNodeToString(res) <> "]"
        end
      "result = " <> Mylib.stringArray_to_string(result_strs) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
