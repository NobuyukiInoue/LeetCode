package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

func maxDepth(root *TreeNode) int {
	// 6ms
	if root == nil {
		return 0
	}
	max_l := maxDepth(root.Left)
	max_r := maxDepth(root.Right)
	if max_l > max_r {
		return max_l + 1
	} else {
		return max_r + 1
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

	result := maxDepth(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
