package solution

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"time"
)

// Definition for a binary tree node.

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var res []int

func preorderTraversal(root *TreeNode) []int {
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
		res = append(res, node.Val)
	}
	if node.Left != nil {
		helper(node.Left)
	}
	if node.Right != nil {
		helper(node.Right)
	}
}

func preorderTraversal2(root *TreeNode) []int {
	// 0ms
	if root == nil {
		return nil
	}
	var (
		stack []*TreeNode
		res   []int
	)
	stack = append(stack, root)
	for len(stack) != 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		res = append(res, node.Val)
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
	}

	return res
}

func intArrayTostring(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(arr[0])
	for i := 1; i < len(arr); i++ {
		resultStr += ", " + strconv.Itoa(arr[i])
	}

	return resultStr
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

	result := preorderTraversal(root)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", intArrayTostring(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
