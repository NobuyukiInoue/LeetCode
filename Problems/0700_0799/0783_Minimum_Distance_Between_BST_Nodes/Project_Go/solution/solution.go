package solution

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

func minDiffInBST(root *TreeNode) int {
	var a []int
	tree := bstToArr(root, a)

	// Sort in descending order.
	sort.Slice(tree, func(a, b int) bool {
		return tree[a] > tree[b]
	})

	minimum := math.MaxInt32
	for i := 0; i < len(tree)-1; i++ {
		minimum = IntMin(tree[i]-tree[i+1], minimum)
	}

	return minimum
}

func bstToArr(node *TreeNode, a []int) []int {
	if node == nil {
		return a
	}

	a = append(a, node.Val)

	// Go all the way right first.
	if node.Right != nil {
		a = bstToArr(node.Right, a)
	}
	if node.Left != nil {
		a = bstToArr(node.Left, a)
	}

	return a
}

func IntMin(a int, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	root := CreateTreeNode(flds)
	fmt.Printf("root = \n%s", TreeToStaircaseString(root))
	fmt.Printf("root = %s\n", Tree2str(root))

	timeStart := time.Now()

	result := minDiffInBST(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
