package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func gardenNoAdj(N int, paths [][]int) []int {
	connects := make([][]int, N)
	for _, p := range paths {
		i, j := p[0]-1, p[1]-1 // i,j = x-1, y-1
		connects[i] = append(connects[i], j)
		connects[j] = append(connects[j], i)
	}
	res := make([]int, N)
	for i := 0; i < N; i++ {
		isUsed := [5]bool{}
		for _, j := range connects[i] {
			isUsed[res[j]] = true
		}
		for color := 1; color <= 4; color++ {
			if !isUsed[color] {
				res[i] = color
				break
			}
		}
	}
	return res
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
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "],[[")

	N, _ := strconv.Atoi(strings.Replace(flds[0], "[[", "", -1))
	data := strings.Split(flds[1], "],[")

	paths := make([][]int, len(data))
	for i := 0; i < len(data); i++ {
		paths[i] = str2IntArray(data[i])
	}

	fmt.Printf("paths = [")
	for i, _ := range paths {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(paths[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(paths[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := gardenNoAdj(N, paths)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", printIntArray(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
