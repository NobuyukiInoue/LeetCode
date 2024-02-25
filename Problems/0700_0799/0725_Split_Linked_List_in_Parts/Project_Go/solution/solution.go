package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func splitListToParts(head *ListNode, k int) []*ListNode {
	// 0ms
	length, node := 0, head
	for node != nil {
		node = node.Next
		length++
	}
	node = head
	part_size, extra := length/k, length%k
	var ans []*ListNode
	for i := 0; i < k; i++ {
		ans = append(ans, node)
		var current_part_size int
		if extra > 0 {
			current_part_size = part_size + 1
		} else {
			current_part_size = part_size
		}
		extra--
		for j := 0; j < current_part_size-1; j++ {
			node = node.Next
		}
		if node != nil {
			node.Next, node = nil, node.Next
		}
	}
	return ans
}

func listListNodeToString(nodes []*ListNode) string {
	res := ""
	for _, lst := range nodes {
		if res == "" {
			res += "[" + ListNodeToString(lst) + "]"
		} else {
			res += ", [" + ListNodeToString(lst) + "]"
		}
	}
	return "[" + res + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	head := CreateListNode(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("head = [%s], k = %d\n", ListNodeToString(head), k)

	timeStart := time.Now()

	result := splitListToParts(head, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", listListNodeToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
