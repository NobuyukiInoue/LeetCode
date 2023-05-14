package solution

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

func deepestLeavesSum(root *TreeNode) int {
	// 55ms - 64ms
	_, x := helper(root, 0, 0, 0)
	return x
}

func helper(root *TreeNode, level, highestLevel, sum int) (int, int) {
	if root.Left != nil {
		highestLevel, sum = helper(root.Left, level+1, highestLevel, sum)
	}

	if root.Right != nil {
		highestLevel, sum = helper(root.Right, level+1, highestLevel, sum)
	}

	if root.Left == nil && root.Right == nil {
		if level > highestLevel {
			highestLevel = level
			sum = root.Val
		} else if level == highestLevel {
			sum += root.Val
		}
	}

	return highestLevel, sum
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

	result := deepestLeavesSum(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
