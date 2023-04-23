package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// 1ms - 3ms
	newHead := head
	a, b := newHead, newHead
	for n > 0 {
		b = b.Next
		n--
	}
	if b == nil {
		return head.Next
	}
	for b.Next != nil {
		b = b.Next
		a = a.Next
	}
	a.Next = a.Next.Next
	return newHead
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	head := CreateListNode(flds[0])
	n, _ := strconv.Atoi(flds[1])
	fmt.Printf("head = %s\n", ListNodeToString(head))
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := removeNthFromEnd(head, n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
