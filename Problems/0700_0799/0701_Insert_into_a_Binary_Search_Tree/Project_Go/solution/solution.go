package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func insertIntoBST(root *TreeNode, val int) *TreeNode {
	// 476ms
	if root == nil {
		return &TreeNode {val, nil, nil}
	}
	if val < root.Val {
		if root.Left == nil {
			root.Left = &TreeNode {val, nil, nil}
		} else {
			insertIntoBST(root.Left, val)
		}
	} else {
		if root.Right == nil {
			root.Right = &TreeNode {val, nil, nil}
		} else {
			insertIntoBST(root.Right, val)
		}
	}
	return root
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	root := CreateTreeNode(flds[0])
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	val, _ := strconv.Atoi(flds[1])
	fmt.Printf("val = %d\n", val)

	timeStart := time.Now()

	result := insertIntoBST(root, val)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
