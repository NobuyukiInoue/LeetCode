package solution

import (
	"fmt"
	"strings"
	"time"
)

func findTilt(root *TreeNode) int {
	ret := 0
	helper(root, &ret)
	return ret
}

func helper(node *TreeNode, ret *int) int {
	if node == nil {
		return 0
	}

	lSum := helper(node.Left, ret)
	rSum := helper(node.Right, ret)
	*ret += IntAbs(lSum - rSum)
	return lSum + rSum + node.Val
}

func IntAbs(x int) int {
	if x >= 0 {
		return x
	} else {
		return -x
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

	result := findTilt(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
