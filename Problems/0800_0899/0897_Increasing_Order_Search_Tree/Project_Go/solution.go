package main

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

func increasingBST(root *TreeNode) *TreeNode {
	return sub_increasingBST(root, nil)
}

func sub_increasingBST(root *TreeNode, tail *TreeNode) *TreeNode {
	if root == nil {
		return tail
	}

	res := sub_increasingBST(root.Left, root)
	root.Left = nil
	root.Right = sub_increasingBST(root.Right, tail)
	return res
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
	fmt.Printf("nums = %s\n", numsStr)

	root := setTreeNode(numsStr)
	fmt.Printf("root = %s", outputTreeNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := increasingBST(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s", outputTreeNode(result))
	fmt.Printf("result = %s\n", Tree2str(root))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
