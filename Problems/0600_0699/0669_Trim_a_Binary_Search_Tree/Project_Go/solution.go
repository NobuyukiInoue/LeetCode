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

func trimBST(root *TreeNode, L int, R int) *TreeNode {
	if root != nil {
		if root.Val > R {
			return trimBST(root.Left, L, R)
		} else if root.Val < L {
			return trimBST(root.Right, L, R)
		}
		root.Left = trimBST(root.Left, L, R)
		root.Right = trimBST(root.Right, L, R)
		return root
	}

	return root
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

	root := setTreeNode(strings.Split(flds[0], ","))
	fmt.Printf("root = %s", outputTreeNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	L, _ := strconv.Atoi(flds[1])
	R, _ := strconv.Atoi(flds[2])

	fmt.Printf("L = %d, R = %d\n", L, R)

	timeStart := time.Now()

	result := trimBST(root, L, R)

	timeEnd := time.Now()

	fmt.Printf("result = %s", outputTreeNode(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
