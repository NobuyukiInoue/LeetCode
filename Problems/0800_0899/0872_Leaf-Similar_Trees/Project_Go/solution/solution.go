package solution

import (
	"fmt"
	"reflect"
	"strconv"
	"strings"
	"time"
)

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	var leaves1, leaves2 []int
	dfs(root1, &leaves1)
	dfs(root2, &leaves2)
	return reflect.DeepEqual(leaves1, leaves2)
}

func dfs(node *TreeNode, leavesOfTree *[]int) {
	if node == nil {
		return
	}
	if node.Left == nil && node.Right == nil {
		*leavesOfTree = append(*leavesOfTree, node.Val)
		return
	}
	dfs(node.Left, leavesOfTree)
	dfs(node.Right, leavesOfTree)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	root1 := CreateTreeNode(flds[0])
	root2 := CreateTreeNode(flds[1])
	fmt.Printf("root1 = %s", TreeToStaircaseString(root1))
	fmt.Printf("root1 = %s\n", Tree2str(root1))
	fmt.Printf("root2 = %s", TreeToStaircaseString(root2))
	fmt.Printf("root2 = %s\n", Tree2str(root2))
	fmt.Println()

	timeStart := time.Now()

	result := leafSimilar(root1, root2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
