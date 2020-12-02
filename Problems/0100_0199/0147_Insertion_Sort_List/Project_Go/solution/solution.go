package solution

import (
	"fmt"
	"strings"
	"time"
)

func insertionSortList(head *ListNode) *ListNode {
	// 4ms
	p := &ListNode{0, nil}
	cur := head
	dummy := p
	dummy.Next = head
	for cur != nil && cur.Next != nil {
		val := cur.Next.Val
		if cur.Val < val {
			cur = cur.Next
			continue
		}

		if p.Next.Val > val {
			p = dummy
		}

		for p.Next.Val < val {
			p = p.Next
		}

		temp := cur.Next
		cur.Next = temp.Next
		temp.Next = p.Next
		p.Next = temp
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

	result := insertionSortList(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
