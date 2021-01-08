package solution

import (
	"fmt"
	"strings"
	"time"
)

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// 16ms
	var s1, s2, s3 []*ListNode

	for l1 != nil {
		s1 = append(s1, l1)
		l1 = l1.Next
	}
	for l2 != nil {
		s2 = append(s2, l2)
		l2 = l2.Next
	}

	carry := 0
	for len(s1) > 0 || len(s2) > 0 {
		var val1, val2 int
		if len(s1) == 0 {
			val1 = 0
		} else {
			val1 = s1[len(s1)-1].Val
			s1 = s1[:len(s1)-1]
		}
		if len(s2) == 0 {
			val2 = 0
		} else {
			val2 = s2[len(s2)-1].Val
			s2 = s2[:len(s2)-1]
		}

		val := val1 + val2 + carry
		node := &ListNode{val % 10, nil}
		carry = val / 10
		s3 = append(s3, node)
	}

	if carry == 1 {
		s3 = append(s3, &ListNode{1, nil})
	}

	dummy := &ListNode{0, nil}
	node := dummy
	for len(s3) > 0 {
		node.Next = s3[len(s3)-1]
		s3 = s3[:len(s3)-1]
		node = node.Next
	}

	return dummy.Next
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
