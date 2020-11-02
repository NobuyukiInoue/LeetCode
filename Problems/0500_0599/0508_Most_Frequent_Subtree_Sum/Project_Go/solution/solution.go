package solution

import (
	"fmt"
	"strings"
	"time"
)

func findFrequentTreeSum(root *TreeNode) []int {
	// 8ms
	count := make(map[int]int)
	dfs(root, count)

	maxVal := 0
	for _, v := range count {
		if v > maxVal {
			maxVal = v
		}
	}

	res := []int{}
	for k, v := range count {
		if v == maxVal {
			res = append(res, k)
		}
	}
	return res
}

func dfs(node *TreeNode, count map[int]int) int {
	if node == nil {
		return 0
	}
	currentSum := node.Val + dfs(node.Left, count) + dfs(node.Right, count)
	count[currentSum]++
	return currentSum
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

	result := findFrequentTreeSum(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
