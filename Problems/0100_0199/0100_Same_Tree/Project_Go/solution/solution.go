package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil || p.Val != q.Val {
		return false
	}
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	l1 := CreateTreeNode(flds[0])
	l2 := CreateTreeNode(flds[1])
	fmt.Printf("l1 = %s", TreeToStaircaseString(l1))
	fmt.Printf("l1 = %s\n", Tree2str(l1))
	fmt.Printf("l2 = %s", TreeToStaircaseString(l2))
	fmt.Printf("l2 = %s\n", Tree2str(l2))
	fmt.Println()

	timeStart := time.Now()

	result := isSameTree(l1, l2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
