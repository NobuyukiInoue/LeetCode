package solution

import (
	"fmt"
	"strings"
	"time"
)

func swapPairs(head *ListNode) *ListNode {
	// 2ms
	node := head
	for node != nil {
		if node.Next == nil {
			break
		}
		temp := node.Val
		node.Val = node.Next.Val
		node.Next.Val = temp
		node = node.Next.Next
	}
	return head
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	head := CreateListNode(flds)
	fmt.Printf("head = [%s]\n", ListNodeToString(head))

	timeStart := time.Now()

	result := swapPairs(head)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
