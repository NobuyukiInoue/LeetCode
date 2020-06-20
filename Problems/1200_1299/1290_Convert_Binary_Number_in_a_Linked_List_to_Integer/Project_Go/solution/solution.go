package solution

import (
	"fmt"
	"strings"
	"time"
)

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func getDecimalValue(head *ListNode) int {
	// 0ms
	total := 0
	for head != nil {
		total <<= 1
		total += head.Val
		head = head.Next
	}
	return total
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	head := setListNode(nums)
	fmt.Printf("head = %s\n", outputListNode(head))

	timeStart := time.Now()

	result := getDecimalValue(head)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
