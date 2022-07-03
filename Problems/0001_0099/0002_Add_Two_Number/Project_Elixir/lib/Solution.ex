defmodule Solution do
  # 546ms - 688ms
  @spec add_two_numbers(l1 :: ListNode.t | nil, l2 :: ListNode.t | nil) :: ListNode.t | nil
  def add_two_numbers(%{val: 0, next: nil}, %{val: 0, next: nil}),
    do: %ListNode{val: 0, next: nil}

  def add_two_numbers(l1, l2) do
    get_value(l1) + get_value(l2) |> from_value()
  end

  def get_value(nil) do
    0
  end

  def get_value(%{val: x, next: y}) do
    x + 10 * get_value(y)
  end

  def from_value(0) do
    nil
  end

  def from_value(x) do
    %ListNode{val: rem(x, 10), next: div(x, 10) |> from_value()}
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")
    nums0 = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    nums1 = for num <- String.split(Enum.at(flds, 1), ","), do: num |> String.trim() |> String.to_integer()
    l1 = OperateListNode.createListNode(nums0)
    l2 = OperateListNode.createListNode(nums1)

    "l1 = [" <> OperateListNode.listNodeToString(l1) <> "]" |> IO.puts()
    "l2 = [" <> OperateListNode.listNodeToString(l2) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.add_two_numbers(l1, l2)
      "result = [" <> OperateListNode.listNodeToString(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
