package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

// 112ms
var sums []int

func maxLevelSum(root *TreeNode) int {
	sums = make([]int, 0)
	dfs(root, 0)
	temp_max, ans := math.MinInt64, 0
	for i, n := range sums {
		if n > temp_max {
			temp_max = n
			ans = i
		}
	}
	return ans + 1
}

func dfs(node *TreeNode, level int) {
	if node == nil {
		return
	}
	if len(sums) <= level {
		sums = append(sums, node.Val)
	} else {
		sums[level] += node.Val
	}
	dfs(node.Left, level+1)
	dfs(node.Right, level+1)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	//	root := CreateTreeNode(flds)
	cd := Constructor()
	root := cd.deserialize(flds) // bad deserialize.
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := maxLevelSum(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
