package solution

import (
	"fmt"
	"strings"
	"time"
)

func middleNode(head *ListNode) *ListNode {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	return slow
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	head := CreateListNode(flds)
	fmt.Printf("head = %s\n", ListNodeToString(head))

	timeStart := time.Now()

	result := middleNode(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
