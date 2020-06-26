package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func detectCycle(head *ListNode) *ListNode {
	// 0ms
	if head == nil || head.Next == nil {
		return nil
	}
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
		if fast == slow {
			for head != fast {
				fast = fast.Next
				head = head.Next
			}
			return head
		}
	}
	return nil
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	head := CreateListNode(flds[0])
	pos, _ := strconv.Atoi(flds[1])
	fmt.Printf("head = %s, pos = %d\n", ListNodeToString(head), pos)

	timeStart := time.Now()

	result := detectCycle(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
