defmodule Solution do
  # 596ms - 654ms
  @spec remove_nodes(head :: ListNode.t | nil) :: ListNode.t | nil
  def remove_nodes(head) when head != nil do
    head = %ListNode{val: head.val, next: remove_nodes(head.next)}
    if head.next != nil and head.val < head.next.val do
      head.next
    else
      head
    end
  end

  def remove_nodes(head) do
    head
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.trim(temp)
    nums =
      if flds != "" do
        for num <- String.split(flds, ","), do: num |> String.trim() |> String.to_integer()
      else
        []
      end

    head = OperateListNode.createListNode(nums)
    "head = [" <> OperateListNode.listNodeToString(head) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.remove_nodes(head)
      "result = [" <> OperateListNode.listNodeToString(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
