package solution

import (
	"fmt"
	"strings"
	"time"
)

func sumRootToLeaf(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return subsumRootToLeaf(root, 0)
}

func subsumRootToLeaf(node *TreeNode, val int) int {
	val = val*2 + node.Val
	if node.Left == node.Right {
		return val
	}
	l, r := 0, 0
	if node.Left != nil {
		l = subsumRootToLeaf(node.Left, val)
	}
	if node.Right != nil {
		r = subsumRootToLeaf(node.Right, val)
	}
	return l + r
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

	result := sumRootToLeaf(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
