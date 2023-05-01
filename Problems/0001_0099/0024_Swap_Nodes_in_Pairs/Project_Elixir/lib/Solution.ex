defmodule Solution do
  # 232ms - 279ms
  @spec swap_pairs(head :: ListNode.t | nil) :: ListNode.t | nil
  def swap_pairs(nil) do
    nil
  end

  def swap_pairs(head) when head.next == nil do
    head
  end

  def swap_pairs(head) do
    %ListNode{val: head.next.val, next: %ListNode{val: head.val, next: swap_pairs(head.next.next)}}
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
      result = Solution.swap_pairs(head)
      "result = [" <> OperateListNode.listNodeToString(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
