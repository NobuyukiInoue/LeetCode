package solution

import (
	"fmt"
	"strings"
	"time"
)

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	// 4ms
	dummy := new(ListNode)
	head := dummy
	for {
		if list1 == nil {
			dummy.Next = list2
			break
		}
		if list2 == nil {
			dummy.Next = list1
			break
		}
		if list1.Val <= list2.Val {
			dummy.Next = list1
			list1 = list1.Next
		} else {
			dummy.Next = list2
			list2 = list2.Next
		}
		dummy = dummy.Next
	}
	return head.Next
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	list1 := CreateListNode(flds[0])
	list2 := CreateListNode(flds[1])
	fmt.Printf("list1 = %s\n", ListNodeToString(list1))
	fmt.Printf("list2 = %s\n", ListNodeToString(list2))

	timeStart := time.Now()

	result := mergeTwoLists(list1, list2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
