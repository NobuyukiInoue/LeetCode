package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

// Definition for a binary tree node.

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	// 28ms
	if t1 == nil {
		return t2
	}
	if t2 == nil {
		return t1
	}
	t1.Val += t2.Val
	t1.Left = mergeTrees(t1.Left, t2.Left)
	t1.Right = mergeTrees(t1.Right, t2.Right)
	return t1
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	t1 := setTreeNode(strings.Split(flds[0], ","))
	fmt.Printf("t1 = %s", outputTreeNode(t1))
	fmt.Printf("t1 = %s\n", Tree2str(t1))

	t2 := setTreeNode(strings.Split(flds[1], ","))
	fmt.Printf("t2 = %s", outputTreeNode(t2))
	fmt.Printf("t2 = %s\n", Tree2str(t2))

	timeStart := time.Now()

	result := mergeTrees(t1, t2)

	timeEnd := time.Now()

	fmt.Printf("result = %s", outputTreeNode(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
