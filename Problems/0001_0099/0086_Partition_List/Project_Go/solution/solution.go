package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func partition(head *ListNode, x int) *ListNode {
	// 0ms
	cur := head
	smaller_sentinel := new(ListNode)
	smaller_cur := smaller_sentinel
	larger_sentinel := new(ListNode)
	larger_cur := larger_sentinel

	for cur != nil {
		if cur.Val < x {
			smaller_cur.Next = cur
			smaller_cur = smaller_cur.Next
		} else {
			larger_cur.Next = cur
			larger_cur = larger_cur.Next
		}
		cur = cur.Next
	}

	larger_cur.Next = nil
	smaller_cur.Next = larger_sentinel.Next
	return smaller_sentinel.Next
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	head := setListNode(nums)
	x, _ := strconv.Atoi(flds[1])
	fmt.Printf("head = %s, x = %d\n", outputListNode(head), x)

	timeStart := time.Now()

	result := partition(head, x)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", outputListNode(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
