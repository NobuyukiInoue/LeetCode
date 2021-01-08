package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func addOneRow(root *TreeNode, v int, d int) *TreeNode {
	// 88ms
	return addOneRowSub(root, v, d, 1, true)
}

func addOneRowSub(root *TreeNode, v int, d int, n int, isLeft bool) *TreeNode {
	if root == nil {
		return nil
	}
	if n == d {
		temp := root
		root = &TreeNode{v, nil, nil}
		if isLeft {
			root.Left = temp
		} else {
			root.Right = temp
		}
	}
	if root.Left != nil {
		root.Left = addOneRowSub(root.Left, v, d, n + 1, true)
	} else if n + 1 == d {
		root.Left = &TreeNode{v, nil, nil}
	}
	if root.Right != nil {
		root.Right = addOneRowSub(root.Right, v, d, n + 1, false)
	} else if n + 1 == d {
		root.Right = &TreeNode{v, nil, nil}
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
	fmt.Printf("root = %s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))
	v, _ := strconv.Atoi(flds[1])
	d, _ := strconv.Atoi(flds[2])
	fmt.Printf("v = %d, d = %d\n", v, d)

	timeStart := time.Now()

	result := addOneRow(root, v, d)

	timeEnd := time.Now()

	fmt.Printf("result = %s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
