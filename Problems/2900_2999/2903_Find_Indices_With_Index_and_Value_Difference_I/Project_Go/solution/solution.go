package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findIndices(nums []int, indexDifference int, valueDifference int) []int {
	// 6ms
	mini, maxi := 0, 0
	for i := indexDifference; i < len(nums); i++ {
		if nums[i-indexDifference] < nums[mini] {
			mini = i - indexDifference
		}
		if nums[i-indexDifference] > nums[maxi] {
			maxi = i - indexDifference
		}
		if nums[i]-nums[mini] >= valueDifference {
			return []int{mini, i}
		}
		if nums[maxi]-nums[i] >= valueDifference {
			return []int{maxi, i}
		}
	}
	return []int{-1, -1}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	indexDifference, _ := strconv.Atoi(flds[1])
	valueDifference, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums = [%s], indexDifference = %d, valueDifference = %d\n", IntArrayToString(nums), indexDifference, valueDifference)

	timeStart := time.Now()

	result := findIndices(nums, indexDifference, valueDifference)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
