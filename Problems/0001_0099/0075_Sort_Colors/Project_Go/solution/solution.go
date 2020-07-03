package solution

import (
	"fmt"
	"strings"
	"time"
)

func sortColors(nums []int)  {
	// 0ms
	red, white, blue := 0, 0, 0
	for _, n := range nums {
		if n == 0 {
			red++
		} else if n == 1 {
			white++
		} else {
			blue++
		}
	}

	i, j := 0, 0
	for j = 0; j < red; j++ {
		nums[i] = 0
		i++
	}
	for j = 0; j < white; j++ {
		nums[i] = 1
		i++
	}
	for j = 0; j < blue; j++ {
		nums[i] = 2
		i++
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	sortColors(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(nums))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
