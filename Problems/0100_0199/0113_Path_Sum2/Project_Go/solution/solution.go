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

func pathSum(root *TreeNode, sum int) [][]int {
	// 4ms
	results := make([][]int, 0)
	tempArr := make([]int, 0)
	helper(root, sum, &results, tempArr)
	return results
}

func helper(root *TreeNode, sum int, results *[][]int, tempArr []int) {
	if root == nil {
		return
	}
	if root.Left == nil && root.Right == nil && sum == root.Val {
		tempArr := append(tempArr, root.Val)
		*results = append(*results, append([]int(nil), tempArr...))
	}
	helper(root.Left, sum-root.Val, results, append(tempArr, root.Val))
	helper(root.Right, sum-root.Val, results, append(tempArr, root.Val))
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

	root := setTreeNode(strings.Split(flds[0], ","))
	fmt.Printf("root = %s", outputTreeNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	sum, _ := strconv.Atoi(flds[1])

	timeStart := time.Now()

	result := pathSum(root, sum)

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
