package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

var res []int

func postorderTraversal(root *TreeNode) []int {
	// 0ms
	res = make([]int, 0)
	if root == nil {
		return nil
	}
	helper(root)
	return res
}

func helper(node *TreeNode) {
	if node != nil {
		res = append([]int{node.Val}, res...)
	}
	if node.Right != nil {
		helper(node.Right)
	}
	if node.Left != nil {
		helper(node.Left)
	}
}

func postorderTraversal2(root *TreeNode) []int {
	// 0ms
	var res []int
	var stack []*TreeNode

	if root == nil {
		return res
	}

	stack = append(stack, root)

	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		res = append([]int{node.Val}, res...)
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}

	return res
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

	result := postorderTraversal(root)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
