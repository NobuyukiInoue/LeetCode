package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func generateParenthesis(n int) []string {
	// 0ms
	res := []string{}
	helper(n, 0, 0, "", &res)
	return res
}

func helper(n, left, right int, temp string, res *[]string) {
	if n == right {
		*res = append(*res, temp)
		return
	}
	if left != n {
		helper(n, left+1, right, temp+"(", res)
	}
	if left > right {
		helper(n, left, right+1, temp+")", res)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := generateParenthesis(n)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
