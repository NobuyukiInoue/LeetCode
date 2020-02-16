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

func oddEvenList(head *ListNode) *ListNode {
	// 4ms
	if head == nil || head.Next == nil {
		return head
	}

	next_head := head.Next
	cursor := head
	count := 1
	var last_odd_node *ListNode

	for cursor != nil {
		if count%2 == 1 {
			last_odd_node = cursor
		}
		temp_next := cursor.Next
		if cursor.Next != nil {
			cursor.Next = cursor.Next.Next
		}
		cursor = temp_next
		count++
	}

	last_odd_node.Next = next_head

	return head
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := strToIntArray(flds)
	fmt.Printf("nums = %s\n", intArrayToString(nums))

	head := setListNode(nums)
	fmt.Printf("head = %s\n", outputListNode(head))

	timeStart := time.Now()

	result := oddEvenList(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", outputListNode(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
