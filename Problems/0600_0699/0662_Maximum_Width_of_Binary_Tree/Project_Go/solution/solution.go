package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

var width []int

func widthOfBinaryTree(root *TreeNode) int {
	// 4ms
	width = make([]int, 0)
	return dfs(root, 1, 0)
}

func dfs(node *TreeNode, id int, depth int) int {
	if node == nil {
		return 0
	}
	if depth >= len(width) {
		width = append(width, id)
	}
	return myMax(id + 1 - width[depth], myMax(dfs(node.Left, id*2, depth + 1), dfs(node.Right, id*2 + 1, depth + 1)))
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
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

	result := widthOfBinaryTree(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
