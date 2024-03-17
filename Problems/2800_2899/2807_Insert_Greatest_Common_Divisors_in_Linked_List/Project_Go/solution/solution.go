package solution

import (
	"fmt"
	"strings"
	"time"
)

func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	// 4ms - 15ms
	node := head
	for node.Next != nil {
		node.Next = &ListNode{gcd(node.Val, node.Next.Val), node.Next}
		node = node.Next.Next
	}
	return head
}

func gcd(num1, num2 int) int {
	if num2 == 0 {
		return num1
	} else {
		return gcd(num2, num1%num2)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	head := CreateListNode(flds)
	fmt.Printf("head = %s\n", ListNodeToString(head))

	timeStart := time.Now()

	result := insertGreatestCommonDivisors(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
