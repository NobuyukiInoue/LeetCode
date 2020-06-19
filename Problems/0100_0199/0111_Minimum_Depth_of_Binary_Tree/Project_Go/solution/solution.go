package solution

import (
	"fmt"
	"strings"
	"time"
)

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	if root.Left != nil && root.Right != nil {
		l := minDepth(root.Left) + 1
		r := minDepth(root.Right) + 1
		return myMin(l, r)
	} else if root.Left != nil {
		return minDepth(root.Left) + 1
	} else if root.Right != nil {
		return minDepth(root.Right) + 1
	} else {
		return 1
	}    
}

func myMin(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	root := CreateTreeNode(flds)
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := minDepth(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
