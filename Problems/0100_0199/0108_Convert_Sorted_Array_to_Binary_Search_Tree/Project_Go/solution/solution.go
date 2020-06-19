package solution

import (
	"fmt"
	"strings"
	"time"
)

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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := sortedArrayToBST(nums)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
