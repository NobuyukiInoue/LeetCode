package solution

import (
	"fmt"
	"strings"
	"time"
)

func levelOrderBottom(root *TreeNode) [][]int {
	// 0ms
	result := [][]int{}
	helper([]*TreeNode{root}, &result)
	return result[1:]
}

func helper(level []*TreeNode, result *[][]int) {
	if len(level) == 0 {
		return
	}
	nextLevel := []*TreeNode{}
	for _, v := range level {
		if v != nil {
			nextLevel = append(nextLevel, v.Left)
			nextLevel = append(nextLevel, v.Right)
		}
	}
	helper(nextLevel, result)
	list := []int{}
	for _, v := range level {
		if v != nil {
			list = append(list, v.Val)
		}
	}
	*result = append(*result, list)
}

func levelOrderBottom2(root *TreeNode) [][]int {
	// 4ms
	result := make([][]int, 0)

	if root == nil {
		return result
	}

	queue := make([]*TreeNode, 0)
	queue = append(queue, root)

	for true {
		nodeCount := len(queue)
		if nodeCount == 0 {
			break
		}

		subList := make([]int, 0)
		for nodeCount > 0 {
			dataNode := queue[0]
			queue = queue[1:]
			subList = append(subList, dataNode.Val)

			if dataNode.Left != nil {
				queue = append(queue, dataNode.Left)
			}
			if dataNode.Right != nil {
				queue = append(queue, dataNode.Right)
			}

			nodeCount--
		}

		tempResult := make([][]int, len(result)+1)
		tempResult[0] = subList
		for i := 0; i < len(result); i++ {
			tempResult[i+1] = result[i]
		}
		result = tempResult
	}

	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	var root *TreeNode

	if len(flds) > 0 {
		root = CreateTreeNode(flds)
	} else {
		root = nil
	}

	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := levelOrderBottom(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
