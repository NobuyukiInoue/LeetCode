package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isPalindrome(head *ListNode) bool {
	// 12ms
	if head == nil {
		return true
	}

	p1 := head
	p2 := head
	p3 := p1.Next
	pre := p1
	for p2.Next != nil && p2.Next.Next != nil {
		p2 = p2.Next.Next
		pre = p1
		p1 = p3
		p3 = p3.Next
		p1.Next = pre
	}

	if p2.Next == nil {
		p1 = p1.Next
	}

	for p3 != nil {
		if p1.Val != p3.Val {
			return false
		}
		p1 = p1.Next
		p3 = p3.Next
	}

	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	head := CreateListNode(flds)
	fmt.Printf("head = %s\n", ListNodeToString(head))

	timeStart := time.Now()

	result := isPalindrome(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
