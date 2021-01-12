package solution

import (
	"fmt"
	"strings"
	"time"
)

var res []*TreeNode

func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
	// 8ms
	res = make([]*TreeNode, 0)
	helper(root, to_delete, true)
	return res
}

func helper(node *TreeNode, to_delete []int, is_root bool) *TreeNode {
	if node == nil {
		return nil
	}
	deleted := contains(to_delete, node.Val)
	if is_root && !deleted {
		res = append(res, node)
	}
	node.Left = helper(node.Left, to_delete, deleted)
	node.Right = helper(node.Right, to_delete, deleted)
	if deleted {
		return nil
	}
	return node
}

func contains(s []int, e int) bool {
	for _, v := range s {
		if e == v {
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
	fmt.Printf("root = %s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	to_delete := StringToIntArray(flds[1])
	fmt.Println()

	timeStart := time.Now()

	result := delNodes(root, to_delete)

	timeEnd := time.Now()

	for i := 0; i < len(result); i++ {
		fmt.Printf("result[%d] = %s", i, TreeToStaircaseString(result[i]))
	}
	fmt.Println()

	for i := 0; i < len(result); i++ {
		fmt.Printf("result[%d] = %s\n", i, Tree2str(result[i]))
	}
	fmt.Println()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
