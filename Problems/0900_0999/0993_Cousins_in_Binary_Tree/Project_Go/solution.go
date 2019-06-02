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

func isCousins(root *TreeNode, x int, y int) bool {
	if root == nil {
		return false
	}

	queue := []*TreeNode{root}
	for len(queue) != 0 {
		size := len(queue)
		tmp := map[int]bool{}
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			tmp[node.Val] = true
			if node.Left != nil && node.Right != nil {
				if (node.Left.Val == x && node.Right.Val == y) ||
					(node.Left.Val == y && node.Right.Val == x) {
					return false
				}
			}
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		if tmp[x] && tmp[y] {
			return true
		}
	}
	return false
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

	x, _ := strconv.Atoi(flds[1])
	y, _ := strconv.Atoi(flds[2])
	fmt.Printf("x = %d, y = %d\n", x, y)

	timeStart := time.Now()

	result := isCousins(root, x, y)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
