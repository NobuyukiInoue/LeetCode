package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
	// 42ms - 45ms
	m := len(l)
	ans := make([]bool, 0)
	for i := 0; i < m; i++ {
		temp := make([]int, r[i]+1-l[i])
		copy(temp, nums[l[i]:r[i]+1])
		sort.Sort(sort.IntSlice(temp))
		ans = append(ans, checkDiff(temp))
	}
	return ans
}

func checkDiff(temp []int) bool {
	diff := temp[1] - temp[0]
	for i := 2; i < len(temp); i++ {
		if temp[i]-temp[i-1] != diff {
			return false
		}
	}
	return true
}

func BoolArrayToString(temp []bool) string {
	if len(temp) <= 0 {
		return ""
	}

	resultStr := strconv.FormatBool(temp[0])
	for i := 1; i < len(temp); i++ {
		resultStr += ", " + strconv.FormatBool(temp[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums := StringToIntArray(flds[0])
	l := StringToIntArray(flds[1])
	r := StringToIntArray(flds[2])
	fmt.Printf("nums = [%s], l = [%s], r = [%s]\n", IntArrayToString(nums), IntArrayToString(l), IntArrayToString(r))

	timeStart := time.Now()

	result := checkArithmeticSubarrays(nums, l, r)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", BoolArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
