package solution

import (
	"fmt"
	"strings"
	"time"
)

func zigzagLevelOrder(root *TreeNode) [][]int {
	// 0ms
	resultList := make([][]int, 0)
	helper(root, &resultList, 0)
	return resultList
}

func helper(node *TreeNode, resultList *[][]int, level int) {
	if node == nil {
		return
	}
	if len(*resultList) < level+1 {
		*resultList = append(*resultList, []int{node.Val})
	} else {
		if level%2 == 0 {
			(*resultList)[level] = append((*resultList)[level], node.Val)
		} else {
			(*resultList)[level] = append([]int{node.Val}, (*resultList)[level]...)
		}
	}
	helper(node.Left, resultList, level+1)
	helper(node.Right, resultList, level+1)
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

	result := zigzagLevelOrder(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
