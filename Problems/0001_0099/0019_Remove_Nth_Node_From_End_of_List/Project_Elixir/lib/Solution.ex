defmodule Solution do
  # 219ms - 258ms
  @spec remove_nth_from_end(head :: ListNode.t | nil, n :: integer) :: ListNode.t | nil
  def remove_nth_from_end(%ListNode{next: nil}, 1) do
    nil
  end

  def remove_nth_from_end(head, 1) do
    head
    |> node_list_to_array()
    |> Enum.slice(1..-1)
    |> array_to_list_node()
  end

  def remove_nth_from_end(%ListNode{} = head, n) do
    n = n - 1
    head = node_list_to_array(head)
    head = Enum.slice(head, 0..(n - 1)) |> Enum.concat(Enum.slice(head, (n + 1)..-1))
    array_to_list_node(head)
  end

  @spec node_list_to_array(node: ListNode.t, array: [integer]) :: [integer]
  @spec node_list_to_array(ListNode.t()) :: nonempty_maybe_improper_list
  def node_list_to_array(list_node) do
    node_list_to_array(list_node, [])
  end
  def node_list_to_array(%ListNode{next: nil, val: elem}, array) do
    [elem | array]
  end

  def node_list_to_array(%ListNode{next: some, val: elem}, array) do
    node_list_to_array(some, [elem | array])
  end

  @spec array_to_list_node(nums: [integer], node: ListNode.t) :: ListNode.t | nil
  def array_to_list_node([h | t]) do
    array_to_list_node(t, %ListNode{next: nil, val: h})
  end

  def array_to_list_node([], last_node) do
    last_node
  end

  def array_to_list_node([h | t], last_node) do
    array_to_list_node(t, %ListNode{next: last_node, val: h})
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")
    nums0 = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    head = OperateListNode.createListNode(nums0)
    n = String.to_integer(Enum.at(flds, 1))

    "head = [" <> OperateListNode.listNodeToString(head) <> "]" |> IO.puts()
    "n = " <> Integer.to_string(n) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.remove_nth_from_end(head, n)
      "result = [" <> OperateListNode.listNodeToString(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
