package solution

import (
	"fmt"
	"strings"
	"time"
)

func average(salary []int) float64 {
	// 0ms
	max, min, sum := salary[0], salary[0], 0
	for _, v  := range salary {
		if v > max {
			max = v
		} else if v < min {
			min = v
		}
		sum += v
	}
	
	return float64(sum - max - min)/float64(len(salary) - 2)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	salary := StringToIntArray(flds)
	fmt.Printf("salary = [%s]\n", IntArrayToString(salary))

	timeStart := time.Now()

	result := average(salary)

	timeEnd := time.Now()

	fmt.Printf("result = %f\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
