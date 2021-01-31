package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func removeLeafNodes(root *TreeNode, target int) *TreeNode {
	// 12ms
	if root == nil {
		return nil
	}
	if root.Left != nil {
		root.Left = removeLeafNodes(root.Left, target)
	}
	if root.Right != nil {
		root.Right = removeLeafNodes(root.Right, target)
	}
	if root.Val == target && root.Left == nil && root.Right == nil {
		root = nil
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

	target, _ := strconv.Atoi(flds[1])
	fmt.Printf("target = %d\n", target)

	timeStart := time.Now()

	result := removeLeafNodes(root, target)

	timeEnd := time.Now()

	cd := Codec{}
	fmt.Printf("result = [%s]\n", cd.serialize(result))
	fmt.Printf("result = %s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
