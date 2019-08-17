package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numEquivDominoPairs(dominoes [][]int) int {
	// 28ms
	res := 0
	count := [100]int{}
	for _, domino := range dominoes {
		d := mapping(domino)
		res += count[d]
		count[d]++
	}
	return res
}

func mapping(A []int) int {
	a, b := A[0], A[1]
	if a < b {
		return a*10 + b
	}
	return b*10 + a
}

func numEquivDominoPairs2(dominoes [][]int) int {
	// 48ms
	hash, pairs := make(map[string]int), 0
	for _, d := range dominoes {
		key, revKey := fmt.Sprintf("%v:%v", d[0], d[1]), fmt.Sprintf("%v:%v", d[1], d[0])
		if occurs, exists := hash[key]; exists {
			pairs += occurs
		}
		hash[key]++
		if d[0] != d[1] {
			hash[revKey]++
		}
	}
	return pairs
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	dominoes := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		dominoes[i] = str2IntArray(flds[i])
	}

	fmt.Printf("dominoes = [")
	for i, _ := range dominoes {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(dominoes[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(dominoes[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := numEquivDominoPairs(dominoes)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
