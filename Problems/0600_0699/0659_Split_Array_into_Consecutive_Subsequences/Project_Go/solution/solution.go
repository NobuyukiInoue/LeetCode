package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isPossible(nums []int) bool {
	// 64ms
	n := len(nums)
	if n < 3 {
		return false
	}

	first, last := nums[0], nums[n-1]

	start := myAbs(first)
	arr := make([]int, start + last + 2)

	for _, num := range(nums) {
		arr[start + num]++
	}

	if last - first < 2 {
		return false
	}

	for first <= last {
		count := 0   
		for i := first; i <= last; i++ {
			if arr[i + start] == 0 {
				if count < 3 {
					return false
				} else {
					break
				}
			}
			if count >= 3 && arr[i - 1 + start] >= arr[i + start] {
					break
			}
			arr[i + start]--
			count++
		}
		
		if count < 3 {
			return false
		}

		for arr[first + start] == 0 && first <= last {
			first++
		}
	}
	return true
}

func myAbs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := isPossible(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
