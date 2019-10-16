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

func buildTree(preorder []int, inorder []int) *TreeNode {
	// 20ms
	return helper(0, 0, len(inorder)-1, preorder, inorder)
}

func helper(preStart int, inStart int, inEnd int, preorder []int, inorder []int) *TreeNode {
	if preStart > len(preorder)-1 || inStart > inEnd {
		return nil
	}

	root := new(TreeNode)
	root.Val = preorder[preStart]
	inIndex := 0

	for i := 0; i <= inEnd; i++ {
		if inorder[i] == root.Val {
			inIndex = i
		}
	}

	root.Left = helper(preStart+1, inStart, inIndex-1, preorder, inorder)
	root.Right = helper(preStart+inIndex-inStart+1, inIndex+1, inEnd, preorder, inorder)
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

	preorder := stringToIntArray(flds[0])
	inorder := stringToIntArray(flds[1])

	fmt.Printf("preorder = [%s]\n", intArrayToString(preorder))
	fmt.Printf("inorder = [%s]\n", intArrayToString(inorder))

	timeStart := time.Now()

	result := buildTree(preorder, inorder)

	timeEnd := time.Now()

	fmt.Printf("result = %s", outputTreeNode(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
