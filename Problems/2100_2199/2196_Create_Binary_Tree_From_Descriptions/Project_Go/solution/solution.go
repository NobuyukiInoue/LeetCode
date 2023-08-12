package solution

import (
	"fmt"
	"strings"
	"time"
)

func createBinaryTree(descriptions [][]int) *TreeNode {
	// 301ms - 324ms
	dic := make(map[int]*TreeNode)
	children := make(map[int]bool)
	for _, des := range descriptions {
		if _, ok := dic[des[0]]; !ok {
			dic[des[0]] = &TreeNode{Val: des[0]}
		}
		if _, ok := dic[des[1]]; !ok {
			dic[des[1]] = &TreeNode{Val: des[1]}
		}
		if des[2] == 1 {
			dic[des[0]].Left = dic[des[1]]
		} else {
			dic[des[0]].Right = dic[des[1]]
		}
		children[des[1]] = true
	}
	for k := range dic {
		if _, ok := children[k]; !ok {
			return dic[k]
		}
	}
	return nil
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	descriptions := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		descriptions[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("descriptions = %s\n", IntIntArrayToGridString(descriptions))

	timeStart := time.Now()

	result := createBinaryTree(descriptions)

	timeEnd := time.Now()

	fmt.Printf("result = %s", TreeToStaircaseString(result))
	fmt.Printf("result = %s\n", Tree2str(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
