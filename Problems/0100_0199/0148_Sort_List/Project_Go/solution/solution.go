package solution

import (
	"fmt"
	"strings"
	"time"
)

func sortList(head *ListNode) *ListNode {
	// 12ms
	if head == nil || head.Next == nil {
		return head
	}

	slow, fast := head, head.Next
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	rightHead := slow.Next
	slow.Next = nil
	h1 := sortList(head)

	return merge(h1, sortList(rightHead))
}

func merge(h1 *ListNode, h2 *ListNode) *ListNode {
	dummy := &ListNode{Val: 0}
	tail := dummy

	for h1 != nil && h2 != nil {
		if h1.Val < h2.Val {
			tail.Next = h1
			h1 = h1.Next
		} else {
			tail.Next = h2
			h2 = h2.Next
		}
		tail = tail.Next
	}

	if h1 != nil {
		tail.Next = h1
	}
	if h2 != nil {
		tail.Next = h2
	}

	return dummy.Next
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	head := CreateListNode(flds)
	fmt.Printf("head = %s\n", ListNodeToString(head))

	timeStart := time.Now()

	result := sortList(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
