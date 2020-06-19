package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

var res []int

func rightSideView(root *TreeNode) []int {
	// 0ms
	res = make([]int, 0)
	helper(root, 1)
	return res
}

func helper(node *TreeNode, level int) {
	if node == nil {
		return
	}

	if len(res) < level {
		res = append(res, node.Val)
	}

	if node.Right != nil {
		helper(node.Right, level+1)
	}

	if node.Left != nil {
		helper(node.Left, level+1)
	}
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

	result := rightSideView(root)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
