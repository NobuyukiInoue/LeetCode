package solution

import (
	"fmt"
	"strings"
	"time"
)

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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	inorder := StringToIntArray(flds[0])
	postorder := StringToIntArray(flds[1])

	fmt.Printf("inorder = [%s]\n", IntArrayToString(inorder))
	fmt.Printf("postorder = [%s]\n", IntArrayToString(postorder))

	timeStart := time.Now()

	result := buildTree(inorder, postorder)

	timeEnd := time.Now()

	fmt.Printf("result = %s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
