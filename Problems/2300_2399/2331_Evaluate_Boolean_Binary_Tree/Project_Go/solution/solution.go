package solution

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"time"
)

func evaluateTree(root *TreeNode) bool {
	// 13ms - 22ms
	return helper(root)
}

func helper(node *TreeNode) bool {
	switch node.Val {
	case 0:
		return false
	case 1:
		return true
	case 2:
		return helper(node.Left) || helper(node.Right)
	case 3:
		return helper(node.Left) && helper(node.Right)
	default:
		return true
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

	result := evaluateTree(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
