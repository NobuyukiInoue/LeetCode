package solution

import (
	"fmt"
	"strings"
	"time"
)

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	carry := 0
	head := new(ListNode)
	cur := head
	for l1 != nil || l2 != nil || carry != 0 {
		n1, n2 := 0, 0
		if l1 != nil {
			n1, l1 = l1.Val, l1.Next
		}
		if l2 != nil {
			n2, l2 = l2.Val, l2.Next
		}
		num := n1 + n2 + carry
		carry = num / 10
		cur.Next = &ListNode{Val: num % 10, Next: nil}
		cur = cur.Next
	}
	return head.Next
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	l1 := CreateListNode(flds[0])
	l2 := CreateListNode(flds[1])
	fmt.Printf("l1 = %s\n", ListNodeToString(l1))
	fmt.Printf("l2 = %s\n", ListNodeToString(l2))

	timeStart := time.Now()

	result := addTwoNumbers(l1, l2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
