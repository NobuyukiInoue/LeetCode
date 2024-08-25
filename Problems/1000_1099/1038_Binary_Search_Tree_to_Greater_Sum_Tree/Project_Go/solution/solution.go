package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

// 1ms
var sum int

func bstToGst(root *TreeNode) *TreeNode {
	sum = 0
	reverseInorderTraversal(root)
	return root
}

func reverseInorderTraversal(node *TreeNode) {
	if node == nil {
		return
	}
	reverseInorderTraversal(node.Right)
	sum += node.Val
	node.Val = sum
	reverseInorderTraversal(node.Left)
}

func LoopMain(args string) {
	// コメント部の削除
	rep := regexp.MustCompile("#.*")
	args = rep.ReplaceAllString(args, "")
	rep = regexp.MustCompile("//.*")
	args = rep.ReplaceAllString(args, "")
	if len(args) == 0 {
		return
	}

	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	root := CreateTreeNode(flds)
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := bstToGst(root)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
