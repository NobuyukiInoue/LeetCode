package main

import (
	"fmt"
	"reflect"
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

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	var leaves1, leaves2 []int
	dfs(root1, &leaves1)
	dfs(root2, &leaves2)
	return reflect.DeepEqual(leaves1, leaves2)
}

func dfs(node *TreeNode, leavesOfTree *[]int) {
	if node == nil {
		return
	}
	if node.Left == nil && node.Right == nil {
		*leavesOfTree = append(*leavesOfTree, node.Val)
		return
	}
	dfs(node.Left, leavesOfTree)
	dfs(node.Right, leavesOfTree)
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

	root1 := setTreeNode(numsStr1)
	root2 := setTreeNode(numsStr2)
	fmt.Printf("root1 = %s", outputTreeNode(root1))
	fmt.Printf("root1 = %s\n", Tree2str(root1))
	fmt.Printf("root2 = %s", outputTreeNode(root2))
	fmt.Printf("root2 = %s\n", Tree2str(root2))
	fmt.Println()

	timeStart := time.Now()

	result := leafSimilar(root1, root2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
