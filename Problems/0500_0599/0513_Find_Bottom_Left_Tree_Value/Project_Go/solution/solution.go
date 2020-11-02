package solution

import (
	"fmt"
	"strings"
	"time"
)

func findBottomLeftValue(root *TreeNode) int {
	// 4ms
	return dfs(root, 1, []int{0, 0})
}

func dfs(root *TreeNode, depth int, res []int) int {
	if res[1] < depth {
		res[0] = root.Val
		res[1] = depth
	}
	if root.Left != nil {
		dfs(root.Left, depth+1, res)
	}
	if root.Right != nil {
		dfs(root.Right, depth+1, res)
	}
	return res[0]
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

	result := findBottomLeftValue(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
