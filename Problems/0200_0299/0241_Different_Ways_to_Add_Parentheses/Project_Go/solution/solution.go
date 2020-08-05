package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func diffWaysToCompute(input string) []int {
	// 0ms
	res := make([]int, 0)
	inputNum, err := strconv.Atoi(input)
	if err == nil {
		res = append(res, inputNum)
		return res
	}

	for i := 0; i < len(input); i++ {
		if input[i] == '+' || input[i] == '-' || input[i] == '*' {
			res_l := diffWaysToCompute(input[:i])
			res_r := diffWaysToCompute(input[i + 1:])
			for _, leftNum := range(res_l) {
				for _, rightNum := range(res_r) {
					res = append(res, calc(leftNum, rightNum, input[i]))
				}
			}
		}
	}
	return res;
}

func calc(m int, n int, ope byte) int {
	if ope == '+' {
		return m + n
	} else if ope == '-' {
		return m - n
	}
	return m * n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	input := strings.Replace(temp, "]", "", -1)
	fmt.Printf("input = %s\n", input)

	timeStart := time.Now()

	result := diffWaysToCompute(input)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
