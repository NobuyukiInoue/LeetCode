package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findJudge(N int, trust [][]int) int {
	l := make([]int, N+1)
	for i, _ := range trust {
		l[trust[i][1]]++
		l[trust[i][0]]--
	}
	for i := 1; i < N+1; i++ {
		if l[i] == N-1 {
			return i
		}
	}

	return -1
}

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[")

	flds0 := strings.Replace(flds[0], "[", "", -1)
	flds0 = strings.Replace(flds0, "]", "", -1)
	N, _ := strconv.Atoi(flds0)
	fmt.Printf("N = %d\n", N)

	flds1 := strings.Split(strings.Replace(flds[1], "]]]", "", -1), "],[")
	trust := make([][]int, len(flds1))
	for i := 0; i < len(flds1); i++ {
		trust[i] = str2IntArray(flds1[i])
	}

	fmt.Printf("trust = [")
	for i, _ := range trust {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(trust[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(trust[i]))
		}
	}
	fmt.Printf("]\n\n")

	timeStart := time.Now()

	result := findJudge(N, trust)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
