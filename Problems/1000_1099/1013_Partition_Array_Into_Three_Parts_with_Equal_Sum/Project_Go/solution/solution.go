package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canThreePartsEqualSum(A []int) bool {
	total := 0
	for _, val := range A {
		total += val
	}

	if total%3 != 0 {
		return false
	}

	subtotal, count, hit := 0, 0, total/3
	for _, val := range A {
		subtotal += val
		if subtotal == hit {
			subtotal = 0
			count++
			continue
		}
	}

	if count == 3 {
		return true
	} else {
		return false
	}
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

	result := canThreePartsEqualSum(A)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
