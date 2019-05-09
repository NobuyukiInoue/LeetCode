package main

import (
	"fmt"
	"math"
	"sort"
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

func minDiffInBST(root *TreeNode) int {
	var a []int
	tree := bstToArr(root, a)

	// Sort in descending order.
	sort.Slice(tree, func(a, b int) bool {
		return tree[a] > tree[b]
	})

	minimum := math.MaxInt32
	for i := 0; i < len(tree)-1; i++ {
		minimum = IntMin(tree[i]-tree[i+1], minimum)
	}

	return minimum
}

func bstToArr(node *TreeNode, a []int) []int {
	if node == nil {
		return a
	}

	a = append(a, node.Val)

	// Go all the way right first.
	if node.Right != nil {
		a = bstToArr(node.Right, a)
	}
	if node.Left != nil {
		a = bstToArr(node.Left, a)
	}

	return a
}

func IntMin(a int, b int) int {
	if a <= b {
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
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	root := setTreeNode(flds)
	fmt.Printf("root = %s", outputTreeNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := minDiffInBST(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
