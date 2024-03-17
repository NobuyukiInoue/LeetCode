defmodule Solution do
  # 312ms - 338ms
  @spec insert_greatest_common_divisors(head :: ListNode.t | nil) :: ListNode.t | nil
  def insert_greatest_common_divisors(head) when head.next != nil do
    %ListNode{val: head.val, next: %ListNode{val: Integer.gcd(head.val, head.next.val), next: insert_greatest_common_divisors(head.next)}}
  end

  def insert_greatest_common_divisors(head) do
    head
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, ", ", ",")
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")

    nums = for num <- String.split(flds, ",") do num |> String.trim() |> String.to_integer() end
    head = OperateListNode.createListNode(nums)
    "head = [" <> OperateListNode.listNodeToString(head) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.insert_greatest_common_divisors(head)
      "result = [" <> OperateListNode.listNodeToString(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
