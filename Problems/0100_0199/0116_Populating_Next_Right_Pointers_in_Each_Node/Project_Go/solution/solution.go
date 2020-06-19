package solution

import (
	"fmt"
	"strings"
	"time"
)

func connect(root *Node) *Node {
	// 0ms
	if root == nil || root.Left == nil || root.Right == nil {
		return root
	}

	root.Left.Next = root.Right
	if root.Next != nil {
		root.Right.Next = root.Next.Left
	}

	connect(root.Left)
	connect(root.Right)
	return root
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	root := createNode(flds)
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := connect(root)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString_with_next(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
