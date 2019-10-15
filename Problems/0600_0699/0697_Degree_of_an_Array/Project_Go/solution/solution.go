package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findShortestSubArray(nums []int) int {
	nmap := make(map[int]int)
	maxnum, degree, min := 0, 0, len(nums)
	max := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		nmap[nums[i]]++
	}

	// find out degree
	for _, v := range nmap {
		if v>degree {
			degree = v
		}
	}
	// deal special case
	if degree == 1 {
		return 1
	}
	// find all candidate num
	for k, v := range nmap {
		if v == degree {
			max[maxnum] = k
			maxnum++
		}
	}
	// find min from all candidate num
	for i := 0; i < maxnum; i++ {
		current := max[i]
		CurrentDegree := degree
		first,last := -1, 0
		for j := 0; j < len(nums) && CurrentDegree > 0; j++ {
			if nums[j] == current{
				if first == -1 {
					first = j
				} else {
					last = j
				}
				CurrentDegree--
			}
		}
		CurrentLength := last - first + 1
		if CurrentLength < min {
			min = CurrentLength
		}
	}
	return min
}

func IntArray2string(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	nums := make([]int, len(flds))
	for i, val := range flds {
		nums[i], _ = strconv.Atoi(val)
	}

	fmt.Printf("nums = %s\n", IntArray2string(nums))

	timeStart := time.Now()

	result := findShortestSubArray(nums)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
