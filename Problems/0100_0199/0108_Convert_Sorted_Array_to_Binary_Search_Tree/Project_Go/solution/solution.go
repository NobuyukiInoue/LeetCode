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

/*
func sortedArrayToBST(nums []int) *TreeNode {
	return sortedArrayToBST_sub(&nums, 0, len(nums)-1)
}

func sortedArrayToBST_sub(nums *[]int, left int, right int) *TreeNode {
	if left > right {
		return nil
	}
	mid := int((right + left) / 2)
	root := new(TreeNode)
	root.Val = (*nums)[mid]
	root.Left = sortedArrayToBST_sub(nums, left, mid-1)
	root.Right = sortedArrayToBST_sub(nums, mid+1, right)
	return root
}
*/
func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	pos := int(len(nums) / 2)
	node := new(TreeNode)
	node.Val = nums[pos]
	if pos > 0 {
		node.Left = sortedArrayToBST(nums[0:pos])
	}
	if pos > 0 && pos+1 < len(nums) {
		node.Right = sortedArrayToBST(nums[pos+1:])
	}
	return node
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

	nums := str2IntArray(flds)
	fmt.Printf("nums = %s\n", printIntArray(nums))

	timeStart := time.Now()

	result := sortedArrayToBST(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s", outputTreeNode(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
