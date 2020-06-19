package solution

import (
	"fmt"
	"strings"
	"time"
)

func increasingBST(root *TreeNode) *TreeNode {
	return sub_increasingBST(root, nil)
}

func sub_increasingBST(root *TreeNode, tail *TreeNode) *TreeNode {
	if root == nil {
		return tail
	}

	res := sub_increasingBST(root.Left, root)
	root.Left = nil
	root.Right = sub_increasingBST(root.Right, tail)
	return res
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

	result := increasingBST(root)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(root))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
