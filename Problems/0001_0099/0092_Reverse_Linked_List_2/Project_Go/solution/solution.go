package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func reverseBetween(head *ListNode, m int, n int) *ListNode {
	// 0ms
	if head == nil {
		return nil
	}

	dummy := new(ListNode)
	dummy.Next = head
	pre := dummy

	for i := 0; i < m-1; i++ {
		pre = pre.Next
	}

	start := pre.Next
	then := start.Next

	for i := 0; i < n-m; i++ {
		start.Next = then.Next
		then.Next = pre.Next
		pre.Next = then
		then = start.Next
	}
	return dummy.Next
}

func StringToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func IntArrayToString(nums []int) string {
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

	head := CreateListNode(flds[0])
	fmt.Printf("head = %s\n", ListNodeToString(head))

	nums1 := strings.Split(flds[1], ",")
	m, _ := strconv.Atoi(nums1[0])
	n, _ := strconv.Atoi(nums1[1])
	fmt.Printf("m = %d, n = %d\n", m, n)

	timeStart := time.Now()

	result := reverseBetween(head, m, n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
