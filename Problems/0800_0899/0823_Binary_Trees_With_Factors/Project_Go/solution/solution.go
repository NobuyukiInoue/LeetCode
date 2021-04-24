package solution

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

func numFactoredBinaryTrees(arr []int) int {
	// 48ms
    dp := make( map[int]int) 
    constant := (int)(math.Pow(10, 9) + 7)
    sort.Ints(arr)
    for i, curNum := range arr{
        for j := 0 ; j < i ; j+=1 {
            factor := arr[j]
            quotient, remainder := curNum / factor, curNum % factor
            if remainder == 0{
                dp[curNum] += dp[factor] * dp[quotient]
            }
        }
        dp[curNum] += 1
    }
    totalCount := 0
    for _, count := range dp{
        totalCount += count
    }
    return totalCount % constant
}

func numFactoredBinaryTrees2(arr []int) int {
	// 56ms
	arrLength := len(arr)
	sort.Sort(sort.IntSlice(arr))
	numbers := map[int64]int64 {}
	for i := 0; i < arrLength; i++ {
		numbers[int64(arr[i])] = int64(i)
	}

	memo := make([]int64, len(arr))
	for i := 0; i < arrLength; i++ {
		memo[i] = 1
	}
	count := int64(0)
	for idx := 0; idx < arrLength; idx++ {
		for i := 0; i <= idx; i++ {
			mul := int64(arr[i])*int64(arr[idx])
			if mul > math.MaxInt64 {
				 break
			}
			pos := numbers[mul]
			var factor int64
			if pos != 0 {
				if arr[i] == arr[idx] {
					factor = 1
				} else {
					factor = 2
				}
				memo[pos] += factor * memo[i] * memo[idx]
			}
		}
		count += memo[idx];
	}
	return (int)(count % 1000000007)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = %s\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := numFactoredBinaryTrees(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
