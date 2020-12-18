package solution

import (
	"fmt"
	"strings"
	"time"
)

func deleteDuplicates(head *ListNode) *ListNode {
	// 4ms
	if head == nil || head.Next == nil {
		return head
	}

	curr := head
	prev := &ListNode{0, head}
	last := prev
	next := head.Next

	for next != nil {
		if next.Val != curr.Val {
			last = curr
		} else {
			for next != nil && curr.Val == next.Val {
				next = next.Next
			}
			last.Next = next
			if next == nil {
				break
			}
		}
		curr = next
		next = next.Next
	}

	return prev.Next
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	head := CreateListNode(flds)
	fmt.Printf("head = %s\n", ListNodeToString(head))

	timeStart := time.Now()

	result := deleteDuplicates(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
