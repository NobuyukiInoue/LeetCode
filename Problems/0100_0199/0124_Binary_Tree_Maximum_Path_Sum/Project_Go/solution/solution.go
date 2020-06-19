package solution

import (
	"fmt"
	"math"
	"regexp"
	"strings"
	"time"
)

var res int

func maxPathSum(root *TreeNode) int {
	// 16ms
	res = math.MinInt64
	oneSideSum(root)
	return res
}

func oneSideSum(node *TreeNode) int {
	if node == nil {
		return 0
	}
	l := myMax(0, oneSideSum(node.Left))
	r := myMax(0, oneSideSum(node.Right))
	res = myMax(res, node.Val+l+r)
	return node.Val + myMax(l, r)
}

func myMax(a int, b int) int {
	if a > b {
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

	result := maxPathSum(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
