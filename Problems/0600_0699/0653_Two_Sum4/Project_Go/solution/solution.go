package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findTarget(root *TreeNode, k int) bool {
	var s []int

	return dfs(root, &s, k)
}

func dfs(root *TreeNode, s *[]int, k int) bool {
	if root == nil {
		return false
	}

	if search(s, k-root.Val) >= 0 {
		return true
	}

	*s = append(*s, root.Val)

	return dfs(root.Left, s, k) || dfs(root.Right, s, k)
}

func search(s *[]int, target int) int {
	for i, data := range *s {
		if data == target {
			return i
		}
	}

	return -1
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

	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("k = %d\n", k)

	timeStart := time.Now()

	result := findTarget(root, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
