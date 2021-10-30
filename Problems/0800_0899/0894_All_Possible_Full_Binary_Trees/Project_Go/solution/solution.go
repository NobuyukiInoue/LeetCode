package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func allPossibleFBT(n int) []*TreeNode {
	// 16ms
	ans := make([]*TreeNode, 0)
	if n%2 == 0 {
		return ans
	}
	if n == 1 {
		ans = append(ans, &TreeNode{0, nil, nil})
		return ans
	}
	for i := 1; i < n; i += 2 {
		Ll := allPossibleFBT(i)
		Lr := allPossibleFBT(n - 1 - i)
		for _, node_l := range Ll {
			for _, node_r := range Lr {
				node := &TreeNode{0, nil, nil}
				node.Left = node_l
				node.Right = node_r
				ans = append(ans, node)
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := allPossibleFBT(n)

	timeEnd := time.Now()

	for i := 0; i < len(result); i++ {
		fmt.Printf("result[%d] = %s", i, TreeToStaircaseString(result[i]))
	}
	fmt.Println()

	for i := 0; i < len(result); i++ {
		fmt.Printf("result[%d] = %s\n", i, Tree2str(result[i]))
	}
	fmt.Println()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
