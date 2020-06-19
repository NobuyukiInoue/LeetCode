package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func searchBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Val == val {
		return root
	}

	result := new(TreeNode)
	result = nil

	if root.Left != nil {
		result = searchBST(root.Left, val)
		if result != nil {
			return result
		}
	}

	if root.Right != nil {
		result = searchBST(root.Right, val)
	}

	return result
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

	val, _ := strconv.Atoi(flds[1])
	fmt.Printf("val = %d\n", val)

	timeStart := time.Now()

	result := searchBST(root, val)

	timeEnd := time.Now()

	fmt.Printf("result = \n%s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
