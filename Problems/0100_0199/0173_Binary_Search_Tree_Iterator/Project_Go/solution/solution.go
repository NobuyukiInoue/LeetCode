package solution

import (
	"fmt"
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

func BSTIteratorMain(cmds []string, mynode *TreeNode) {
	BI := Constructor(mynode)
	isExistBI := false

	for _, cmd := range cmds {
		if cmd == "BSTIterator" {
			// BI = new BSTIterator(mynode);
			fmt.Printf("BSTIterator iterator = new BSTIterator(root);\n")
			isExistBI = true
		} else if cmd == "next" && isExistBI {
			fmt.Printf("iterator.next();\t ... %d\n", BI.Next())
		} else if cmd == "hasNext" && isExistBI {
			fmt.Printf("iterator.hasNext();\t ... %s\n", strconv.FormatBool(BI.HasNext()))
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)

	flds := strings.Split(temp, "],[[[")
	cmds := strings.Split(strings.Replace(flds[0], "[[", "", -1), ",")

	nodeFlds := strings.Split(flds[1], "]],[")
	fmt.Printf("nodeFlds = %s\n", nodeFlds[0])
	nodeNums := strings.Split(nodeFlds[0], ",")
	mynode := setTreeNode(nodeNums)
	fmt.Printf("mynode = %s", outputTreeNode(mynode))
	fmt.Printf("mynode = %s\n", Tree2str(mynode))

	timeStart := time.Now()

	BSTIteratorMain(cmds, mynode)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
