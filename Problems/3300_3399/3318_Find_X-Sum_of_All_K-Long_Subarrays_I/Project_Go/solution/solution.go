package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func findXSum(nums []int, k int, x int) []int {
	// 8ms - 15ms
	n := len(nums)
	answer := make([]int, n-k+1)
	calculateXSum := func(subarray []int) int {
		frequencyMap := make(map[int]int)

		for _, value := range subarray {
			frequencyMap[value]++
		}

		freqSlice := make([][2]int, 0, len(frequencyMap))
		for key, count := range frequencyMap {
			freqSlice = append(freqSlice, [2]int{key, count})
		}

		sort.Slice(freqSlice, func(i, j int) bool {
			if freqSlice[i][1] == freqSlice[j][1] {
				return freqSlice[i][0] > freqSlice[j][0]
			}
			return freqSlice[i][1] > freqSlice[j][1]
		})

		sum := 0
		for i := 0; i < x && i < len(freqSlice); i++ {
			sum += freqSlice[i][0] * freqSlice[i][1]
		}

		return sum
	}

	for i := 0; i <= n-k; i++ {
		subarray := nums[i : i+k]
		answer[i] = calculateXSum(subarray)
	}

	return answer
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	x, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums = %s, k = %d, x = %d\n", IntArrayToString(nums), k, x)

	timeStart := time.Now()

	result := findXSum(nums, k, x)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
