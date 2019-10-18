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

func buildTree(postorder []int, inorder []int) *TreeNode {
	// 16ms
	return helper(inorder, len(inorder)-1, 0, postorder, len(postorder)-1)
}

func helper(inorder []int, inStart int, inEnd int, postorder []int, postStart int) *TreeNode {
	if postStart < 0 || inStart < inEnd {
		return nil
	}

	root := new(TreeNode)
	root.Val = postorder[postStart]
	rIndex := inStart

	for i := inStart; i >= inEnd; i-- {
		if inorder[i] == postorder[postStart] {
			rIndex = i
			break
		}
	}

	root.Right = helper(inorder, inStart, rIndex+1, postorder, postStart-1)
	root.Left = helper(inorder, rIndex-1, inEnd, postorder, postStart-(inStart-rIndex)-1)
	return root
}

func stringToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	inorder := stringToIntArray(flds[0])
	postorder := stringToIntArray(flds[1])

	fmt.Printf("inorder = [%s]\n", intArrayToString(inorder))
	fmt.Printf("postorder = [%s]\n", intArrayToString(postorder))

	timeStart := time.Now()

	result := buildTree(inorder, postorder)

	timeEnd := time.Now()

	fmt.Printf("result = %s", outputTreeNode(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
