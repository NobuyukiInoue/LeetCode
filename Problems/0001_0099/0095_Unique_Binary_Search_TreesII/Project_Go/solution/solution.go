package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func generateTrees(n int) []*TreeNode {
	// 4ms
	list := []*TreeNode {}

	if n == 0 {
		return list
	}
	return generate(1, n)
}

func generate(left int, right int) []*TreeNode {
	list := []*TreeNode {}

	if left > right {
		return list
	}
	if left == right {
		return append(list, &TreeNode { left, nil, nil })
	}

	for curr := left; curr <= right; curr++ {
		leftChild := generate(left, curr-1)
		rightChild := generate(curr+1, right)

		if len(leftChild) != 0 && len(rightChild) != 0 {
			for _, leftRoot := range(leftChild) {
				for _, rightRoot := range(rightChild) {
					list = append(list, &TreeNode { curr, leftRoot, rightRoot })
				}
			}
		} else if len(leftChild) != 0 {
			for _, leftRoot := range(leftChild) {
				list = append(list, &TreeNode{curr, leftRoot, nil})
			}
		} else if len(rightChild) != 0 {
			for _, rightRoot := range(rightChild) {
				list = append(list, &TreeNode { curr, nil, rightRoot })
			}
		}
	}
	return list
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(flds)

	timeStart := time.Now()

	result := generateTrees(n)

	timeEnd := time.Now()

	for i, _ := range result {
		fmt.Printf("result[%d] = %s", i, TreeToStaircaseString(result[i]))
		fmt.Printf("result[%d] = %s\n", i, Tree2str(result[i]))
		fmt.Println()
	}

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
