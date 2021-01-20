package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	// 12ms
	res := make([]*TreeNode, 0)
	cache := make(map[string]int, 0)
	postorder(root, cache, &res)
	return res
}

func postorder(cur *TreeNode, myMap map[string]int, res *[]*TreeNode) string {
	if cur == nil {
		return "#"
	}
	serial := strconv.Itoa(cur.Val) + "," + postorder(cur.Left, myMap, res) + "," + postorder(cur.Right, myMap, res)
	myMap[serial]++
	if myMap[serial] == 2 {
		*res = append(*res, cur)
	}
	return serial
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

	result := findDuplicateSubtrees(root)

	timeEnd := time.Now()

	fmt.Printf("result = [")
	for i := 0; i < len(result); i++ {
		if i == 0 {
			fmt.Printf(" [%s]", Tree2str(result[i]))
		} else {
			fmt.Printf(", [%s]", Tree2str(result[i]))
		}
	}
	fmt.Printf(" ]\n")
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
