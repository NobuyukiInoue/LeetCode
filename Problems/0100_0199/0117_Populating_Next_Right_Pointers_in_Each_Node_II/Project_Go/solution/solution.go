package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

// Definition for a Node.
type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func connect(root *Node) *Node {
	// 0ms
	node := root
	tail := new(Node)
	dummy := tail
	for node != nil {
		tail.Next = node.Left
		if tail.Next != nil {
			tail = tail.Next
		}
		tail.Next = node.Right
		if tail.Next != nil {
			tail = tail.Next
		}
		node = node.Next
		if node == nil {
			tail = dummy
			node = dummy.Next
		}
	}
	return root
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
	temp = strings.Replace(temp, "[", "", -1)

	flds := strings.Replace(temp, "]", "", -1)
	numsStr := strings.Split(flds, ",")

	fmt.Printf("nums = %s\n", numsStr)

	root := setNode(numsStr)
	fmt.Printf("root = \n%s", outputNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := connect(root)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", outputNode_with_next(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
