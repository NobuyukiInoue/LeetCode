package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func removeNodes2(head *ListNode) *ListNode {
	// 288ms - 296ms
	if head != nil {
		head.Next = removeNodes2(head.Next)
		if head.Next != nil && head.Val < head.Next.Val {
			return head.Next
		}
	}
	return head
}

func removeNodes(head *ListNode) *ListNode {
	// 228ms - 248ms
	head = reverseList(head)
	maximum := math.MinInt32
	current := head
	var prev *ListNode
	for current != nil {
		tmp_next := current.Next
		if current.Val >= maximum {
			maximum = current.Val
			if prev != nil {
				prev.Next = current
				current.Next = nil
			} else {
				head.Next = nil
			}
			prev = current
		}
		current = tmp_next
	}
	return reverseList(head)
}

func reverseList(head *ListNode) *ListNode {
	current := head
	var prev *ListNode
	for current != nil {
		old_next := current.Next
		current.Next = prev
		prev = current
		current = old_next
	}
	return prev
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	head := CreateListNode(flds)
	fmt.Printf("head = %s\n", ListNodeToString(head))

	timeStart := time.Now()

	result := removeNodes(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
