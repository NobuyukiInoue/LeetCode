package solution

import (
	"fmt"
	"strings"
	"time"
)

func candy(ratings []int) int {
	// 16ms
	candies := make([]int, len(ratings))
	for i := 0; i < len(candies); i++ {
		candies[i] = 1
	}
	for i := 1; i < len(ratings); i++ {
		if ratings[i] > ratings[i-1] {
			candies[i] = candies[i-1] + 1
		}
	}
	for i := len(ratings) - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] && candies[i] <= candies[i+1] {
			candies[i] = candies[i+1] + 1
		}
	}
	return mySum(candies)
}

func mySum(nums []int) int {
	res := 0
	for _, num := range nums {
		res += num
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	ratings := StringToIntArray(flds)
	fmt.Printf("ratings = %s\n", IntArrayToString(ratings))

	timeStart := time.Now()

	result := candy(ratings)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
