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

func findTarget(root *TreeNode, k int) bool {
	var s []int

	return dfs(root, &s, k)
}

func dfs(root *TreeNode, s *[]int, k int) bool {
	if root == nil {
		return false
	}

	if search(s, k-root.Val) >= 0 {
		return true
	}

	*s = append(*s, root.Val)

	return dfs(root.Left, s, k) || dfs(root.Right, s, k)
}

func search(s *[]int, target int) int {
	for i, data := range *s {
		if data == target {
			return i
		}
	}

	return -1
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
	k, _ := strconv.Atoi(flds[1])

	fmt.Printf("nums1 = %s\n", numsStr1)

	root := setTreeNode(numsStr1)
	fmt.Printf("root = %s", outputTreeNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	fmt.Println()

	timeStart := time.Now()

	result := findTarget(root, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
