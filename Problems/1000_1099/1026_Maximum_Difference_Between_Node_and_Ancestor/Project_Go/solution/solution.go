package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

// 0ms - 5ms

var maxDiff int

func maxAncestorDiff(root *TreeNode) int {
	maxDiff = 0
	helper(root, root.Val, root.Val)
	return maxDiff
}

func helper(node *TreeNode, v_min int, v_max int) {
	if node == nil {
		return
	}
	maxDiff = myMax(maxDiff, myAbs(v_min-node.Val))
	maxDiff = myMax(maxDiff, myAbs(v_max-node.Val))
	v_min = myMin(v_min, node.Val)
	v_max = myMax(v_max, node.Val)
	helper(node.Left, v_min, v_max)
	helper(node.Right, v_min, v_max)
}

func myAbs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}
func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	// コメント部の削除
	rep := regexp.MustCompile("#.*")
	args = rep.ReplaceAllString(args, "")
	rep = regexp.MustCompile("//.*")
	args = rep.ReplaceAllString(args, "")
	if len(args) == 0 {
		return
	}

	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	root := CreateTreeNode(flds)
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := maxAncestorDiff(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
