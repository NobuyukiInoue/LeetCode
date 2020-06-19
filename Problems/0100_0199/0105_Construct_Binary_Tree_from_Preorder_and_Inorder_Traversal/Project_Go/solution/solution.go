package solution

import (
	"fmt"
	"strings"
	"time"
)

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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	preorder := StringToIntArray(flds[0])
	inorder := StringToIntArray(flds[1])

	fmt.Printf("preorder = [%s]\n", IntArrayToString(preorder))
	fmt.Printf("inorder = [%s]\n", IntArrayToString(inorder))

	timeStart := time.Now()

	result := buildTree(preorder, inorder)

	timeEnd := time.Now()

	fmt.Printf("result = %s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
