package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func kWeakestRows(mat [][]int, k int) []int {
	// 8ms
	mat_length := len(mat)
	soldierTable := make([][]int, mat_length)
	for i := 0; i < mat_length; i++ {
		soldierTable[i] = make([]int, 2)
		soldierTable[i][0] = i
		soldierTable[i][1] = countSoldier(mat[i])
	}

	sort.SliceStable(soldierTable, func(i, j int) bool { return soldierTable[i][1] < soldierTable[j][1] })
	res := make([]int, k)
	for i := 0; i < k; i++ {
		res[i] = soldierTable[i][0]
	}
	return res
}

func countSoldier(arr []int) int {
	res := 0
	for _, i := range arr {
		if i == 1 {
			res++
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
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	str_mat := strings.Split(flds[0], "],[")
	mat := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		mat[i] = str2IntArray(str_mat[i])
	}

	fmt.Printf("mat = [")
	for i, _ := range mat {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(mat[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(mat[i]))
		}
	}
	fmt.Printf("]\n")

	k, _ := strconv.Atoi(strings.Replace(flds[1], "]]", "", -1))

	timeStart := time.Now()

	result := kWeakestRows(mat, k)

	timeEnd := time.Now()

	fmt.Printf("result = [")
	for i, _ := range result {
		if i == 0 {
			fmt.Printf("%d", result[i])
		} else {
			fmt.Printf(",%d", result[i])
		}
	}
	fmt.Printf("]\n")

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
