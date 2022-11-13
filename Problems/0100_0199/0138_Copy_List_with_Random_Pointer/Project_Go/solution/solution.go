package solution

import (
	"fmt"
	"strings"
	"time"
)

func copyRandomList(head *Node) *Node {
	// 0ms - 7ms
	if head == nil {
		return nil
	}

	cur := head
	for cur != nil {
		next := cur.Next
		cur.Next = &Node{cur.Val, nil, nil}
		cur.Next.Next = next
		cur = next
	}

	cur = head
	for cur != nil {
		if cur.Random != nil {
			cur.Next.Random = cur.Random.Next
		}
		cur = cur.Next.Next
	}

	cur = head
	copyHead := head.Next
	for cur != nil {
		next := cur.Next.Next
		copy := cur.Next
		cur.Next = next
		if next != nil {
			copy.Next = next.Next
		}
		cur = next
	}
	return copyHead
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	var head *Node
	if flds[0] == "[]" || flds[0] == "" {
		head = nil
	} else {
		head = CreateNode(flds)
	}
	fmt.Printf("head = %s\n", NodeToString(head))

	timeStart := time.Now()

	result := copyRandomList(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", NodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
