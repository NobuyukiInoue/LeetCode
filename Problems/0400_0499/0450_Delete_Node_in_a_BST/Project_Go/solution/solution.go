package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func deleteNode(root *TreeNode, key int) *TreeNode {
	// 320ms
	if root == nil {
		return root
	}
	if root.Val > key {
		root.Left = deleteNode(root.Left, key)
	} else if root.Val < key {
		root.Right = deleteNode(root.Right, key)
	} else {
		if root.Right == nil {
			return root.Left
		}
		if root.Left == nil {
			return root.Right
		}
		temp := root.Right
		mini := temp.Val
		for temp.Left != nil {
			temp = temp.Left
			mini = temp.Val
		}
		root.Val = mini
		root.Right = deleteNode(root.Right, root.Val)
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
	key, _ := strconv.Atoi(flds[1])
	fmt.Println()

	timeStart := time.Now()

	result := deleteNode(root, key)

	timeEnd := time.Now()

	fmt.Printf("result = %s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
