package solution

import (
	"fmt"
	"strings"
	"strconv"
	"time"
)

func isBalanced(root *TreeNode) bool {
	return isBalancedSub(root, 0) >= 0
}

func isBalancedSub(root *TreeNode, height int) int {
	if root == nil {
		return height
	}

	leftTree := isBalancedSub(root.Left, height+1)
	rightTree := isBalancedSub(root.Right, height+1)

	if leftTree < 0 || rightTree < 0 || abs(leftTree-rightTree) > 1 {
		return -1
	}

	return max(leftTree, rightTree)
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func abs(a int) int {
	if a >= 0 {
		return a
	} else {
		return -a
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

	result := isBalanced(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
