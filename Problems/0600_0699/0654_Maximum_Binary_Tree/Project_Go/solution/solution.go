package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func constructMaximumBinaryTree(nums []int) *TreeNode {
	// 56ms
	if len(nums) == 0 {
		return nil
	}
	return subconstructMaximumBinaryTree(nums, 0, len(nums))
}

func subconstructMaximumBinaryTree(nums []int, start int, end int) *TreeNode {
	if start >= end {
		return nil
	}
	pos := maxnode(nums, start, end)
	node := TreeNode{nums[pos], nil, nil}
	node.Left = subconstructMaximumBinaryTree(nums, start, pos)
	node.Right = subconstructMaximumBinaryTree(nums, pos+1, end)
	return &node
}

func maxnode(nums []int, start int, end int) int {
	maxnum := math.MinInt64
	pos := -1
	for i := start; i < end; i++ {
		if nums[i] > maxnum {
			maxnum = nums[i]
			pos = i
		}
	}
	return pos
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := constructMaximumBinaryTree(nums)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
