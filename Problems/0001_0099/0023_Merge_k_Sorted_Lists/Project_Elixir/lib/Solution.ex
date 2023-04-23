defmodule Solution do
  # 274ms - 281ms
  @spec merge_k_lists(lists :: [ListNode.t | nil]) :: ListNode.t | nil
  def merge_k_lists(lists) when lists == nil, do: nil
  def merge_k_lists([]), do: nil
  def merge_k_lists(lists) do
    lists
    |> Enum.reduce([], fn l, acc -> [make_list(l)| acc] end)
    |> List.flatten()
    |> Enum.sort(:desc)
    |> Enum.reduce( nil, fn n, acc ->
        %ListNode{ val: n, next: acc }
    end)
  end

  defp make_list(nil), do: []
  defp make_list(%{val: val, next: next}) do
    [make_list(next) | [val]]
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
