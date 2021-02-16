package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countBalls(lowLimit int, highLimit int) int {
	// 24ms
	dic := map[int]int{}
	maxCount := 0
	for i := lowLimit; i <= highLimit; i++ {
		num, digits := i, 0
		for num > 0 {
			digits += num%10
			num /= 10;
		}
		dic[digits] += 1
		if dic[digits] > maxCount {
			maxCount = dic[digits]
		}
	}
	return maxCount
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	flds := strings.Split(temp, "],[")

	lowLimit, _  := strconv.Atoi(flds[0]);
	highLimit, _ := strconv.Atoi(flds[1]);
	
	fmt.Printf("lowLimit = %d, hightLimit = %d\n", lowLimit, highLimit)

	timeStart := time.Now()

	result := countBalls(lowLimit, highLimit)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
