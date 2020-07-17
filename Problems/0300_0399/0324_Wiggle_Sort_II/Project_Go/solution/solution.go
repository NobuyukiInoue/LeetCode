package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func wiggleSort(nums []int) {
	// 24ms
	sort.Sort(sort.IntSlice(nums))
	numsLength := len(nums)
	for i := 0; i < numsLength/2; i++ {
	    temp := nums[i]
	    nums[i] = nums[numsLength - 1 - i]
	    nums[numsLength - 1 - i] = temp
	}
	arr := append([]int{}, nums...)
	j := 0
	for i := 1; i < numsLength; i += 2 {
	    nums[i] = arr[j]
	    j++
	}
	for i := 0; i < numsLength; i += 2 {
	    nums[i] = arr[j]
	    j++
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

	wiggleSort(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(nums))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
