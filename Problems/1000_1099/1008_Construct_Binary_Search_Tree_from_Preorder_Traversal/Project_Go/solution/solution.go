package solution

import (
	"fmt"
	"strings"
	"time"
)

func bstFromPreorder(preorder []int) *TreeNode {
	// 0ms
	if preorder == nil {
		return nil
	}
	node := &TreeNode{preorder[0], nil, nil}
	for i := 1; i < len(preorder); i++ {
		helper(node, preorder[i])
	}
	return node
}

func helper(node *TreeNode, val int) *TreeNode {
	if node == nil {
		node = &TreeNode{val, nil, nil}
		return node
	}
	if val < node.Val {
		node.Left = helper(node.Left, val)
	} else {
		node.Right = helper(node.Right, val)
	}
	return node
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	preorder := StringToIntArray(flds)

	timeStart := time.Now()

	result := bstFromPreorder(preorder)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
