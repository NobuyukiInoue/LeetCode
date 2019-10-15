package solution

import (
	"fmt"
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

var result = make([]string, 0)

func binaryTreePaths(root *TreeNode) []string {
	result = make([]string, 0)

	if root == nil {
		return result
	}

	subtree(root, strconv.Itoa(root.Val))
	return result
}

func subtree(node *TreeNode, path string) {
	if node.Left == nil && node.Right == nil {
		result = append(result, path)
	}

	if node.Left != nil {
		subtree(node.Left, path+"->"+strconv.Itoa(node.Left.Val))
	}

	if node.Right != nil {
		subtree(node.Right, path+"->"+strconv.Itoa(node.Right.Val))
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	root := setTreeNode(flds)
	fmt.Printf("root = %s", outputTreeNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := binaryTreePaths(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
