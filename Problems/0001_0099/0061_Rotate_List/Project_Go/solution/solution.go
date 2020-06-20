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

func rotateRight(head *ListNode, k int) *ListNode {
	// 0ms
	if head == nil || head.Next == nil {
		return head
	}

	dummy := new(ListNode)
	dummy.Next = head
	fast, slow := dummy, dummy

	var i, j int
	for i = 0; fast.Next != nil; i++ {
		fast = fast.Next
	}

	for j = i - k%i; j > 0; j-- {
		slow = slow.Next
	}

	fast.Next = dummy.Next
	dummy.Next = slow.Next
	slow.Next = nil

	return dummy.Next
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	head := setListNode(nums)
	fmt.Printf("head = %s, k = %d\n", outputListNode(head), k)

	timeStart := time.Now()

	result := rotateRight(head, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", outputListNode(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
