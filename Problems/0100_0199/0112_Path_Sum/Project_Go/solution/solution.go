package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hasPathSum(root *TreeNode, targetSum int) bool {
	// 8ms
	if root == nil {
		return false
	}
	if root.Left == nil && root.Right == nil {
		return root.Val == targetSum
	}
	if root.Left != nil {
		if hasPathSum(root.Left, targetSum-root.Val) {
			return true
		}
	}
	if root.Right != nil {
		if hasPathSum(root.Right, targetSum-root.Val) {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	root := CreateTreeNode(flds[0])
	targetSum, _ := strconv.Atoi(flds[1])
	fmt.Printf("root = %s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	fmt.Println()

	timeStart := time.Now()

	result := hasPathSum(root, targetSum)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
