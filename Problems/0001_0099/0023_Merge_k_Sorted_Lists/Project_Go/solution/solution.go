package solution

import (
	"fmt"
	"strings"
	"time"
)

func mergeKLists(lists []*ListNode) *ListNode {
	// 7ms - 11ms
	if lists == nil || len(lists) == 0 {
		return nil
	}
	return mergeKListsHelper(lists, 0, len(lists)-1)
}

func mergeKListsHelper(lists []*ListNode, start, end int) *ListNode {
	if start == end {
		return lists[start]
	}
	if start+1 == end {
		return merge(lists[start], lists[end])
	}
	mid := start + (end-start)/2
	left := mergeKListsHelper(lists, start, mid)
	right := mergeKListsHelper(lists, mid+1, end)
	return merge(left, right)
}

func merge(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := ListNode{Val: 0}
	curr := &dummy
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			curr.Next = l1
			l1 = l1.Next
		} else {
			curr.Next = l2
			l2 = l2.Next
		}
		curr = curr.Next
	}
	if l1 != nil {
		curr.Next = l1
	} else {
		curr.Next = l2
	}
	return dummy.Next
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	lists := make([]*ListNode, len(flds))
	for i, _ := range flds {
		lists[i] = CreateListNode(flds[0])
		fmt.Printf("lists[%d] = [%s]\n", i, ListNodeToString(lists[i]))
	}

	timeStart := time.Now()

	result := mergeKLists(lists)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", ListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
