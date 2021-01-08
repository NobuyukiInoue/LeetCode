package solution

import "strconv"

func CreateListNode(flds string) *ListNode {
	if len(flds) <= 0 {
		return nil
	}
	return createSubListNode(StringToIntArray(flds), 0)
}

func createSubListNode(nums []int, index int) *ListNode {
	if nums == nil {
		return nil
	}

	if index >= len(nums) {
		return nil
	}

	node := new(ListNode)
	node.Val = nums[index]
	node.Next = createSubListNode(nums, index+1)

	return node
}

func ListNodeToString(node *ListNode) string {
	if node == nil {
		return ""
	}

	resultStr := strconv.Itoa(node.Val)

	if node.Next != nil {
		resultStr += " -> " + ListNodeToString(node.Next)
	}

	return (resultStr)
}
