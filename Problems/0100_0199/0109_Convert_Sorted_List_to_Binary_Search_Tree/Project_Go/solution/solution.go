package solution

import (
	"fmt"
	"strings"
	"time"
)

func sortedListToBST(head *ListNode) *TreeNode {
	// 428ms
	if head == nil {
		return nil
	}

	dummy := new(ListNode)
	dummy.Next = head
	slow, fast := dummy, dummy

	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	mid := slow.Next
	slow.Next = nil

	return &TreeNode{
		mid.Val,
		sortedListToBST(dummy.Next),
		sortedListToBST(mid.Next),
	}
}

func sortedListToBST2(head *ListNode) *TreeNode {
	// 452ms
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return &TreeNode{Val: head.Val}
	}

	fast, slow := head, head

	if fast != nil && fast.Next != nil {
		fast = fast.Next.Next
	}

	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}

	node := new(TreeNode)
	node.Val = slow.Next.Val
	node.Right = sortedListToBST(slow.Next.Next)
	slow.Next = nil
	node.Left = sortedListToBST(head)

	return node
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	head := setListNode(nums)
	fmt.Printf("head = %s\n", outputListNode(head))

	timeStart := time.Now()

	result := sortedListToBST(head)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
