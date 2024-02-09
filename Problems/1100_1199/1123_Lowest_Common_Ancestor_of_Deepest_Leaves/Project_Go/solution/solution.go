package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

/*
// 4ms - 7ms
type Result struct {
	Depth int
	Node  *TreeNode
}

func lcaDeepestLeaves(root *TreeNode) *TreeNode {
	res := getDeepestNode(root, 0)
	return res.Node
}

func getDeepestNode(node *TreeNode, depth int) *Result {
	if node == nil {
		return &Result{0, nil}
	}
	left := getDeepestNode(node.Left, depth+1)
	right := getDeepestNode(node.Right, depth+1)
	if left.Depth > right.Depth {
		return &Result{left.Depth + 1, left.Node}
	}
	if left.Depth < right.Depth {
		return &Result{right.Depth + 1, right.Node}
	}
	return &Result{left.Depth + 1, node}
}
*/

// 3ms - 6ms
func lcaDeepestLeaves(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	left := height(root.Left)
	right := height(root.Right)
	if left == right {
		return root
	} else if left > right {
		return lcaDeepestLeaves(root.Left)
	} else {
		return lcaDeepestLeaves(root.Right)
	}
}

func height(node *TreeNode) int {
	if node == nil {
		return 0
	}
	return 1 + myMax(height(node.Left), height(node.Right))
}

func myMax(a, b int) int {
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

	result := lcaDeepestLeaves(root)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
