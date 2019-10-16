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

func zigzagLevelOrder(root *TreeNode) [][]int {
	// 0ms
	resultList := make([][]int, 0)
	helper(root, &resultList, 0)
	return resultList
}

func helper(node *TreeNode, resultList *[][]int, level int) {
	if node == nil {
		return
	}
	if len(*resultList) < level+1 {
		*resultList = append(*resultList, []int{node.Val})
	} else {
		if level%2 == 0 {
			(*resultList)[level] = append((*resultList)[level], node.Val)
		} else {
			(*resultList)[level] = append([]int{node.Val}, (*resultList)[level]...)
		}
	}
	helper(node.Left, resultList, level+1)
	helper(node.Right, resultList, level+1)
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

	result := zigzagLevelOrder(root)

	timeEnd := time.Now()

	fmt.Printf("result = [")
	for i := 0; i < len(result); i++ {
		if i == 0 {
			fmt.Printf("[%s]", intArrayToString(result[i]))
		} else {
			fmt.Printf(",[%s]", intArrayToString(result[i]))
		}
	}
	fmt.Printf("]\n")

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
