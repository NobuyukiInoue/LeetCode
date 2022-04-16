package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func findClosestElements(arr []int, k int, x int) []int {
	// 32ms - 93ms
	left, right := 0, len(arr)-1
	for right-left+1 != k {
		if myAbs(arr[left]-x) > myAbs(arr[right]-x) {
			left++
		} else {
			right--
		}
	}
	return arr[left : right+1]
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func findClosestElements_1liner(arr []int, k int, x int) []int {
	// 42ms - 55ms
	return arr[sort.Search(len(arr)-k, func(i int) bool { return x-arr[i] <= arr[i+k]-x }):][:k]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	arr := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	x, _ := strconv.Atoi(flds[2])
	fmt.Printf("arr = [%s], k = %d, x = %d\n", IntArrayToString(arr), k, x)

	timeStart := time.Now()

	result := findClosestElements(arr, k, x)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
