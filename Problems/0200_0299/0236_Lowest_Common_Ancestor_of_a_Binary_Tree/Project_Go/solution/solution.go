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

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
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

	numsStr := strings.Split(flds[0], ",")
	fmt.Printf("nums = %s\n", numsStr)
	root := setTreeNode(numsStr)
	fmt.Printf("root = %s", outputTreeNode(root))
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
