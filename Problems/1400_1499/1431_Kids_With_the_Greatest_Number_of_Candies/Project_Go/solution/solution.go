package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func kidsWithCandies(candies []int, extraCandies int) []bool {
	// 0ms
	max := myMax(candies)
	res := make([]bool, len(candies))
	for i, v := range candies {
		if v+extraCandies >= max {
			res[i] = true
		} else {
			res[i] = false
		}
	}

	return res
}

func myMax(nums []int) int {
	max := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] > max {
			max = nums[i]
		}
	}
	return max
}

func boolArrayToString(data []bool) string {
	if len(data) <= 0 {
		return ""
	}

	resultStr := strconv.FormatBool(data[0])
	for i := 1; i < len(data); i++ {
		resultStr += ", " + strconv.FormatBool(data[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	candies := StringToIntArray(flds[0])
	extraCandies, _ := strconv.Atoi(flds[1])

	fmt.Printf("candies = [%s], extraCandies = %d\n", IntArrayToString(candies), extraCandies)

	timeStart := time.Now()

	result := kidsWithCandies(candies, extraCandies)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", boolArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
