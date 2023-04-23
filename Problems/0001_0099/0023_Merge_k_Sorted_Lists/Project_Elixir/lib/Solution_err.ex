defmodule Solution_Error_CannotAllocateMemory do
  # eheap_alloc: Cannot allocate 255489152 bytes of memory (of type "heap").
  # Crash dump is being written to: erl_crash.dump...
  # lists =
  # [[],[],[],[],[],[],[],[],[],[],[]]
  #
  @spec merge_k_lists(lists :: [ListNode.t | nil]) :: ListNode.t | nil
  def merge_k_lists(lists) when lists == nil or lists == [] do
    nil
  end

  def merge_k_lists(lists) do
    merge_k_lists_helper(lists, 0, Enum.count(lists) - 1)
  end

  @spec merge_k_lists_helper(lists :: [ListNode.t | nil], i_start :: integer, i_end :: integer) :: ListNode.t | nil
  def merge_k_lists_helper(lists, i_start, i_end) when i_start == i_end do
    Enum.at(lists, i_start)
  end

  def merge_k_lists_helper(lists, i_start, i_end) when i_start + 1 == i_end do
    merge(Enum.at(lists, i_start), Enum.at(lists, i_end))
  end

  def merge_k_lists_helper(lists, i_start, i_end) do
    i_mid = div(i_start + (i_end - i_start), 2)
    left = merge_k_lists_helper(lists, i_start, i_mid)
    right = merge_k_lists_helper(lists, i_mid + 1, i_end)
    merge(left, right)
  end

  @spec merge(l1 :: ListNode.t | nil, l2 :: ListNode.t | nil) :: ListNode.t | nil
  def merge(l1, l2) do
    merge_while(l1, l2)
  end

  @spec merge_while(l1 :: ListNode.t | nil, l2 :: ListNode.t | nil) :: ListNode.t | nil
  def merge_while(l1, l2) when l1 != nil and l2 != nil do
    if l1.val < l2.val do
      %ListNode{val: l1.val, next: merge_while(l1.next, l2)}
    else
      %ListNode{val: l2.val, next: merge_while(l1, l2.next)}
    end
  end

  def merge_while(l1, _) when l1 != nil do
    %ListNode{val: l1.val, next: l1.next}
  end

  def merge_while(_, l2) when l2 != nil do
    %ListNode{val: l2.val, next: l2.next}
  end

  def merge_while(_, _) do
    nil
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    lists =
      cond do
        temp == "" ->
          nil
        flds == [] ->
          nil
        Enum.count(flds) == 0 ->
          []
        true ->
          for i <- 0..Enum.count(flds) - 1 do
            cur =
              if Enum.at(flds, i) == "" do
                nil
              else
                nums = for num <- String.split(Enum.at(flds, i), ","), do: num |> String.trim() |> String.to_integer()
                OperateListNode.createListNode(nums)
              end
            "lists[" <> Integer.to_string(i) <> "] = [" <> OperateListNode.listNodeToString(cur) <> "]" |> IO.puts()
            cur
      end
    end

    exectime = Benchmark.measure(fn ->
      result = Solution.merge_k_lists(lists)
      "result = [" <> OperateListNode.listNodeToString(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
