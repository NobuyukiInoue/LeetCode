package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func trimBST(root *TreeNode, L int, R int) *TreeNode {
	if root != nil {
		if root.Val > R {
			return trimBST(root.Left, L, R)
		} else if root.Val < L {
			return trimBST(root.Right, L, R)
		}
		root.Left = trimBST(root.Left, L, R)
		root.Right = trimBST(root.Right, L, R)
		return root
	}

	return root
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	root := CreateTreeNode(flds[0])
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	L, _ := strconv.Atoi(flds[1])
	R, _ := strconv.Atoi(flds[2])

	fmt.Printf("L = %d, R = %d\n", L, R)

	timeStart := time.Now()

	result := trimBST(root, L, R)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
