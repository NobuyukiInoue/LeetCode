package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkStraightLine(coordinates [][]int) bool {
	// 4ms
	dx := (float64)(coordinates[1][0] - coordinates[0][0])
	if dx == 0.0 {
		return false
	}
	inclination := (float64)(coordinates[1][1]-coordinates[0][1]) / dx
	for i := 1; i < len(coordinates)-1; i++ {
		dx = (float64)(coordinates[i+1][0] - coordinates[i][0])
		if dx == 0 {
			return false
		}
		if (float64)(coordinates[i+1][1]-coordinates[i][1])/dx != inclination {
			return false
		}
	}
	return true
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

	coordinates := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		coordinates[i] = str2IntArray(flds[i])
	}

	fmt.Printf("coordinates = [")
	for i, _ := range coordinates {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(coordinates[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(coordinates[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := checkStraightLine(coordinates)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
