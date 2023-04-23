defmodule Solution_use_map do
  # 263ms - 285ms
  @spec merge_k_lists(lists :: [ListNode.t | nil]) :: ListNode.t | nil
  def merge_k_lists(lists) when lists == nil, do: nil
  def merge_k_lists([]), do: nil
  def merge_k_lists([node]), do: node
  def merge_k_lists(lists) do
    Stream.chunk_every(lists, 2)
    |> Enum.map(&merge/1)
    |> merge_k_lists()
  end

  defp merge([list1]), do: list1
  defp merge([list1, list2]) do
    merge_two(list1, list2, nil)
  end

  defp merge_two(list1, nil, ans), do: reverse(ans, list1)
  defp merge_two(nil, list2, ans), do: reverse(ans, list2)
  defp merge_two(list1, list2, ans) when list1.val < list2.val do
    merge_two(list1.next, list2, %{list1 | next: ans})
  end
  defp merge_two(list1, list2, ans) do
    merge_two(list1, list2.next, %{list2 | next: ans})
  end

  defp reverse(nil, tail), do: tail
  defp reverse(list, tail) do
    reverse(list.next, %{list | next: tail})
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
