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

func sumNumbers(root *TreeNode) int {
	// 0ms
	return helper(root, 0)
}

func helper(node *TreeNode, sumVal int) int {
	if node == nil {
		return sumVal
	}
	sumVal = sumVal*10 + node.Val
	if node.Left == nil && node.Right == nil {
		return sumVal
	}
	sumLeft, sumRight := 0, 0
	if node.Left != nil {
		sumLeft = helper(node.Left, sumVal)
	}
	if node.Right != nil {
		sumRight = helper(node.Right, sumVal)
	}
	return sumLeft + sumRight
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
	temp = strings.Replace(temp, "]", "", -1)

	flds := strings.Split(temp, ",")
	root := setTreeNode(flds)
	fmt.Printf("root = %s", outputTreeNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := sumNumbers(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
