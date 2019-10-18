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

func flatten(root *TreeNode) {
	// 4ms
	helper(root)
}

func helper(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	left := helper(root.Left)
	right := helper(root.Right)
	if left == nil && right == nil {
		return root
	} else if left != nil {
		temp := root.Right
		root.Right = root.Left
		root.Left = nil
		left.Right = temp
		if right == nil {
			return left
		}
	}
	return right
}

func intArrayToString(nums []int) string {
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

	flatten(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s", outputTreeNode(root))
	fmt.Printf("result = %s\n", Tree2str(root))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
