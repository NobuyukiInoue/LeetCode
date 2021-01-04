package solution

import (
	"fmt"
	"strings"
	"time"
)

// 8ms
var res []int

func largestValues(root *TreeNode) []int {
	res = make([]int, 0)
	dfs(root, 0)
	return res
}

func dfs(node *TreeNode, level int) {
	if node == nil {
		return
	}
	if level > len(res)-1 {
		res = append(res, node.Val)
	} else if node.Val > res[level] {
		res[level] = node.Val
	}

	dfs(node.Left, level+1)
	dfs(node.Right, level+1)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	var root *TreeNode
	if len(flds) > 0 {
		root = CreateTreeNode(flds)
	} else {
		root = nil
	}
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := largestValues(root)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
