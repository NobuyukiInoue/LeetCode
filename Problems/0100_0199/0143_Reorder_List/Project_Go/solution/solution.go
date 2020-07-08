package solution

import (
	"fmt"
	"strings"
	"time"
)

func reorderList(head *ListNode)  {
	// 16ms
	if head == nil || head.Next == nil {
		return
	}

	//Find the middle of the list
	p1, p2 := head, head
	for p2.Next != nil && p2.Next.Next != nil { 
		p1, p2 = p1.Next, p2.Next.Next;
	}

	//Reverse the half after middle  1->2->3->4->5->6 to 1->2->3->6->5->4
	preMiddle, preCurrent := p1, p1.Next;
	for preCurrent.Next != nil {
		current := preCurrent.Next
		preCurrent.Next = current.Next
		current.Next = preMiddle.Next
		preMiddle.Next = current
	}

	//Start reorder one by one  1->2->3->6->5->4 to 1->6->2->5->3->4
	p1 = head
	p2 = preMiddle.Next
	for p1 != preMiddle {
		preMiddle.Next = p2.Next
		p2.Next = p1.Next
		p1.Next = p2
		p1 = p2.Next
		p2 = preMiddle.Next
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	head := CreateListNode(flds)
	fmt.Printf("head = %s\n", ListNodeToString(head))

	timeStart := time.Now()

	reorderList(head)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ListNodeToString(head))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
