package solution

import (
	"fmt"
	"strings"
	"time"
)

func oddEvenList(head *ListNode) *ListNode {
	// 4ms
	if head == nil || head.Next == nil {
		return head
	}

	next_head := head.Next
	cursor := head
	count := 1
	var last_odd_node *ListNode

	for cursor != nil {
		if count%2 == 1 {
			last_odd_node = cursor
		}
		temp_next := cursor.Next
		if cursor.Next != nil {
			cursor.Next = cursor.Next.Next
		}
		cursor = temp_next
		count++
	}

	last_odd_node.Next = next_head

	return head
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	head := CreateListNode(flds)
	fmt.Printf("head = %s\n", ListNodeToString(head))

	timeStart := time.Now()

	result := oddEvenList(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
