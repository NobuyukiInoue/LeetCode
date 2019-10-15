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

func longestUnivaluePath(root *TreeNode) int {
	res := make([]int, 1)

	if root != nil {
		dfs(root, res)
	}

	return res[0]
}

func dfs(node *TreeNode, res []int) int {
	var l int
	var r int

	if node.Left != nil {
		l = dfs(node.Left, res)
	} else {
		l = 0
	}

	if node.Right != nil {
		r = dfs(node.Right, res)
	} else {
		r = 0
	}

	var resl int
	var resr int
	if node.Left != nil && node.Left.Val == node.Val {
		resl = l + 1
	} else {
		resl = 0
	}

	if node.Right != nil && node.Right.Val == node.Val {
		resr = r + 1
	} else {
		resr = 0
	}

	res[0] = IntMax(res[0], resl+resr)

	return IntMax(resl, resr)
}

func IntMax(a int, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	numsStr := strings.Split(flds, ",")

	root := setTreeNode(numsStr)
	fmt.Printf("root = %s", outputTreeNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	fmt.Println()

	timeStart := time.Now()

	result := longestUnivaluePath(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
