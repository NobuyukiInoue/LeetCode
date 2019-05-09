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

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil || p.Val != q.Val {
		return false
	}
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	numsStr1 := strings.Split(flds[0], ",")
	numsStr2 := strings.Split(flds[1], ",")

	fmt.Printf("nums1 = %s\n", numsStr1)
	fmt.Printf("nums2 = %s\n", numsStr2)

	l1 := setTreeNode(numsStr1)
	l2 := setTreeNode(numsStr2)
	fmt.Printf("l1 = %s", outputTreeNode(l1))
	fmt.Printf("l1 = %s\n", Tree2str(l1))
	fmt.Printf("l2 = %s", outputTreeNode(l2))
	fmt.Printf("l2 = %s\n", Tree2str(l2))
	fmt.Println()

	timeStart := time.Now()

	result := isSameTree(l1, l2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)}
