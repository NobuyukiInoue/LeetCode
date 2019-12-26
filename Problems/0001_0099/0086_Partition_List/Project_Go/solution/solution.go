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

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := str2IntArray(flds[0])
	fmt.Printf("nums = %s\n", printIntArray(nums))

	head := setListNode(nums)
	x, _ := strconv.Atoi(flds[1])
	fmt.Printf("head = %s, x = %d\n", outputListNode(head), x)

	timeStart := time.Now()

	result := partition(head, x)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", outputListNode(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
