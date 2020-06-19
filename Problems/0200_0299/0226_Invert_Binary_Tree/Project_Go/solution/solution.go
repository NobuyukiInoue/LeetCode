package solution

import (
	"fmt"
	"strings"
	"time"
)

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	t := root.Left
	root.Left = root.Right
	root.Right = t
	invertTree(root.Left)
	invertTree(root.Right)

	return root
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	root := CreateTreeNode(flds)
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	fmt.Println()

	timeStart := time.Now()

	result := invertTree(root)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
