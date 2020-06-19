package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	// 8ms
	if root == p || root == q {
		return root
	}
	if root == nil {
		return nil
	}
	left := lowestCommonAncestor(root.Left, p, q)
	right := lowestCommonAncestor(root.Right, p, q)
	if left != nil && right != nil {
		return root
	}
	if left != nil {
		return left
	}
	return right
}

func setTargetNode(node *TreeNode, target int) *TreeNode {
	if node == nil {
		return nil
	}
	if node.Val == target {
		return node
	}
	left := setTargetNode(node.Left, target)
	if left != nil {
		return left
	}
	right := setTargetNode(node.Right, target)
	return right
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	nump, _ := strconv.Atoi(flds[1])
	numq, _ := strconv.Atoi(flds[2])

	root := CreateTreeNode(flds[0])
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	p := setTargetNode(root, nump)
	q := setTargetNode(root, numq)

	fmt.Printf("p = %s, q = %s\n", Tree2str(p), Tree2str(q))

	timeStart := time.Now()

	result := lowestCommonAncestor(root, p, q)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
