defmodule Solution do
  # 327ms - 511ms
  @spec delete_duplicates(head :: ListNode.t | nil) :: ListNode.t | nil
  def delete_duplicates(nil) do
    nil
  end

  def delete_duplicates(%ListNode{val: _, next: nil} = current_node) do
    current_node
  end

  def delete_duplicates(%ListNode{val: val, next: %ListNode{val: val, next: _} = next_node} = _current_node) do
    delete_duplicates(next_node)
  end

  def delete_duplicates(%ListNode{val: _, next: next_node} = current_node) do
    %ListNode{current_node | next: delete_duplicates(next_node)}
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")
    nums = for num <- String.split(flds, ","), do: num |> String.trim() |> String.to_integer()
    head = OperateListNode.createListNode(nums)
    "head = [" <> OperateListNode.listNodeToString(head) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.delete_duplicates(head)
      "result = [" <> OperateListNode.listNodeToString(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
