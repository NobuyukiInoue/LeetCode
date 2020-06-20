package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func prefixesDivBy5(A []int) []bool {
	total := 0
	lenA := len(A)
	result := make([]bool, lenA)
	for i := 0; i < lenA; i++ {
		//total = (total*2 + A[i]) % 5
		total = ((total << 1) + A[i]) % 5
		if total == 0 {
			result[i] = true
		} else {
			result[i] = false
		}
	}
	return result
}

func BoolArrayToString(nums []bool) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.FormatBool(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.FormatBool(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	A := StringToIntArray(flds)
	fmt.Printf("A = [%s]\n", IntArrayToString(A))

	timeStart := time.Now()

	result := prefixesDivBy5(A)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", BoolArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
