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

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root.Val > p.Val && root.Val > q.Val {
		return lowestCommonAncestor(root.Left, p, q)
	} else if root.Val < p.Val && root.Val < q.Val {
		return lowestCommonAncestor(root.Right, p, q)
	} else {
		return root
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	numsStr0 := strings.Split(flds[0], ",")
	numsStr1 := strings.Split(flds[1], ",")
	numsStr2 := strings.Split(flds[2], ",")

	fmt.Printf("nums0 = %s\n", numsStr0)
	fmt.Printf("nums1 = %s\n", numsStr1)
	fmt.Printf("nums2 = %s\n", numsStr2)

	root := setTreeNode(numsStr0)
	fmt.Printf("root = %s", outputTreeNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	p := setTreeNode(numsStr1)
	q := setTreeNode(numsStr2)
	fmt.Printf("p = %s, q = %s\n", Tree2str(p), Tree2str(q))

	timeStart := time.Now()

	result := lowestCommonAncestor(root, p, q)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
