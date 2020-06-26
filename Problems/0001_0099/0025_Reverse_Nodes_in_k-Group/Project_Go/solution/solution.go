package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func reverseKGroup(head *ListNode, k int) *ListNode {
	curr := head
	count := 0

	for curr != nil && count != k {
		curr = curr.Next
		count++
	}

	if count == k {
		curr = reverseKGroup(curr, k)
		for ; count > 0; count-- {
			tmp := head.Next
			head.Next = curr
			curr = head
			head = tmp
		}
		head = curr
	}
	return head
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	head := CreateListNode(flds[0])

	k, err := strconv.Atoi(flds[1])
	if err != nil {
		fmt.Printf("%s can not conv to integer.\n", flds[1])
		return
	}

	fmt.Printf("head = %s, k = %d\n", ListNodeToString(head), k)

	timeStart := time.Now()

	result := reverseKGroup(head, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
