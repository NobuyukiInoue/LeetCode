package main

import "strconv"

func setListNode(nums []int) *ListNode {
	return setListNode2(nums, 0)
}

func setListNode2(nums []int, index int) *ListNode {
	if nums == nil {
		return nil
	}

	if index >= len(nums) {
		return nil
	}

	node := new(ListNode)
	node.Val = nums[index]
	node.Next = setListNode2(nums, index+1)

	return node
}

func outputListNode(node *ListNode) string {
	if node == nil {
		return ""
	}

	resultStr := strconv.Itoa(node.Val)

	if node.Next != nil {
		resultStr += " -> " + outputListNode(node.Next)
	}

	return (resultStr)
}
