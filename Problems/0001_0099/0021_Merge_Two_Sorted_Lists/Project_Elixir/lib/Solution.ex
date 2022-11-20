defmodule Solution do
  # 410ms - 481ms
  @spec merge_two_lists(list1 :: ListNode.t | nil, list2 :: ListNode.t | nil) :: ListNode.t | nil
  def merge_two_lists(nil, nil), do: nil
  def merge_two_lists(list1, nil), do: list1
  def merge_two_lists(nil, list2), do: list2

  def merge_two_lists(%ListNode{val: valist1, next: next1} = _list1, %ListNode{val: valist2} = list2) when valist1 <= valist2 do
    %ListNode{val: valist1, next: merge_two_lists(next1, list2)}
  end

  def merge_two_lists(%ListNode{val: _valist1} = list1, %ListNode{val: valist2, next: next2} = _list2) do
    %ListNode{val: valist2, next: merge_two_lists(list1, next2)}
  end

  @spec set_list(flds :: [String.t], index :: integer) :: ListNode.t | nil
  def set_list(flds, index) do
    if Enum.count(flds) == 0 do
      nil
    else
      if Enum.at(flds, index) == "" do
        nil
      else
        nums = for num <- String.split(Enum.at(flds, index), ","), do: num |> String.trim() |> String.to_integer()
        OperateListNode.createListNode(nums)
      end
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")
    list1 = set_list(flds, 0)
    list2 = set_list(flds, 1)
    "list1 = [" <> OperateListNode.listNodeToString(list1) <> "]" |> IO.puts()
    "list2 = [" <> OperateListNode.listNodeToString(list2) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.merge_two_lists(list1, list2)
      "result = [" <> OperateListNode.listNodeToString(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
