package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hasCycle(head *ListNode) bool {
	// 7ms - 8ms
	if head == nil {
		return false
	}
	fastPtr, slowPtr := head, head
	for fastPtr != nil && fastPtr.Next != nil {
		fastPtr = fastPtr.Next.Next
		slowPtr = slowPtr.Next
		if fastPtr == slowPtr {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	head := CreateListNode(flds)
	fmt.Printf("head = %s\n", ListNodeToString(head))

	timeStart := time.Now()

	result := hasCycle(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
