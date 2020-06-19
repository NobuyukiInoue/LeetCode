package solution

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"time"
)

var res int
var count int

func kthSmallest(root *TreeNode, k int) int {
	// 8ms
	count = k
	res = 0
	helper(root)
	return res
}

func helper(node *TreeNode) {
	if node == nil {
		return
	}
	helper(node.Left)
	count--
	if count == 0 {
		res = node.Val
		return
	}
	helper(node.Right)
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	root := CreateTreeNode(flds[0])
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	k, _ := strconv.Atoi(flds[1])

	timeStart := time.Now()

	result := kthSmallest(root, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
