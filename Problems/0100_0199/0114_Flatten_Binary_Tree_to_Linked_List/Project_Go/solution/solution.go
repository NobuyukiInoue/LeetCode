package solution

import (
	"fmt"
	"strings"
	"time"
)

func flatten(root *TreeNode) {
	// 4ms
	helper(root)
}

func helper(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	left := helper(root.Left)
	right := helper(root.Right)
	if left == nil && right == nil {
		return root
	} else if left != nil {
		temp := root.Right
		root.Right = root.Left
		root.Left = nil
		left.Right = temp
		if right == nil {
			return left
		}
	}
	return right
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

	flatten(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s", TreeToStaircaseString(root))
	fmt.Printf("result = %s\n", Tree2str(root))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
