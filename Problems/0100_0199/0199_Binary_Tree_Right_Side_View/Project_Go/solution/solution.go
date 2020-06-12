package solution

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"time"
)

// Definition for a binary tree node.

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

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

func intArrayTostring(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := ""
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr
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
	temp = strings.Replace(temp, "]", "", -1)

	flds := strings.Split(temp, ",")
	root := setTreeNode(flds)
	fmt.Printf("root = %s", outputTreeNode(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := rightSideView(root)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", intArrayTostring(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
