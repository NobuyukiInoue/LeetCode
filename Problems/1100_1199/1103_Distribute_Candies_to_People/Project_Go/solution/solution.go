package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func distributeCandies(candies int, num_people int) []int {
	res := make([]int, num_people)
	for i := 0; candies > 0; i++ {
		res[i%num_people] += min(candies, i+1)
		candies -= i + 1
	}
	return res
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	candies, _ := strconv.Atoi(flds[0])
	num_people, _ := strconv.Atoi(flds[1])

	fmt.Printf("candies = %d, num_people = %d\n", candies, num_people)
	timeStart := time.Now()

	result := distributeCandies(candies, num_people)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
