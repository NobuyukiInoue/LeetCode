package solution

import (
	"fmt"
	"strings"
	"time"
)

var ans int;

func goodNodes(root *TreeNode) int {
	// 100ms
	ans = 0
	dfs(root, root.Val)
	return ans
}

func dfs(node *TreeNode, curMax int) {
	if node == nil {
		return
	}
	if node.Val >= curMax {
		curMax = node.Val
		ans++
	}
	dfs(node.Left, curMax)
	dfs(node.Right, curMax)
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

	result := goodNodes(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
