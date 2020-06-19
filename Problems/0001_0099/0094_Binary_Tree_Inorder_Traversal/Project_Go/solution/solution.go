package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

func inorderTraversal(root *TreeNode) []int {
	// 0ms
	resultList := make([]int, 0)
	helper(root, &resultList)
	return resultList
}

func helper(node *TreeNode, resultList *[]int) {
	if node == nil {
		return
	}
	helper(node.Left, resultList)
	*resultList = append(*resultList, node.Val)
	helper(node.Right, resultList)
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

	result := inorderTraversal(root)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
