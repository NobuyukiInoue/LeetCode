package solution

import (
	"fmt"
	"strings"
	"time"
)

const intSize = 32 << (^uint(0) >> 63)

func findSecondMinimumValue(root *TreeNode) int {
	//	fmt.Printf("intmax = %d\n", IntPow(2, 31)-1)
	res := helper(root, root.Val)
	if res != IntPow(2, 31)-1 {
		return res
	}
	return -1
}

func helper(root *TreeNode, preVal int) int {
	if root == nil {
		return IntPow(2, 31) - 1
	}
	if root.Val > preVal {
		return root.Val
	}

	return IntMin(helper(root.Left, root.Val), helper(root.Right, root.Val))
}

func IntMin(a int, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}

func IntPow(x int, y int) int {
	result := 1
	for i := 0; i < y; i++ {
		result *= x
	}
	return result
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

	result := findSecondMinimumValue(root)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
