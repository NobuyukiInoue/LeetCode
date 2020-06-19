package solution

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"time"
)

func isValidBST(root *TreeNode) bool {
	// 4ms
	var stack []*TreeNode
	max := -1 << 63
	for nd := root; nd != nil || len(stack) != 0; {
		for nd != nil {
			stack = append(stack, nd)
			nd = nd.Left
		}
		if len(stack) != 0 {
			nd = stack[len(stack)-1]
			if nd.Val > max {
				max = nd.Val
			} else {
				return false
			}
			stack = stack[:len(stack)-1]
			nd = nd.Right
		}
	}
	return true
}

func isValidBST2(root *TreeNode) bool {
	// 8ms
	return helper(root, nil, nil)
}

func helper(root, l, r *TreeNode) bool {
	if root == nil {
		return true
	}
	left, right := true, true
	if l != nil {
		left = l.Val < root.Val
	}
	if r != nil {
		right = root.Val < r.Val
	}
	return left && right && helper(root.Left, l, root) && helper(root.Right, root, r)
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

	result := isValidBST(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
