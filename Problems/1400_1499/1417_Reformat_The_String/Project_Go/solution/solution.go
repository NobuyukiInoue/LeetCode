package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func reformat(s string) string {
	// 0ms
	nums := make([]byte, len(s))
	letters := make([]byte, len(s))
	numsCount, lettersCount := 0, 0

	for i := 0; i < len(s); i++ {
		if 0x30 <= s[i] && s[i] <= 0x39 {
			nums[numsCount] = s[i]
			numsCount++
		} else {
			letters[lettersCount] = s[i]
			lettersCount++
		}
	}

	if math.Abs(float64(numsCount-lettersCount)) > 1 {
		return ""
	}

	res := make([]byte, len(s))
	k := 0
	if lettersCount > numsCount {
		for x := 0; x < lettersCount; x++ {
			res[k] = letters[x]
			k += 2
		}
		k = 1
		for y := 0; y < numsCount; y++ {
			res[k] = nums[y]
			k += 2
		}
	} else {
		for y := 0; y < numsCount; y++ {
			res[k] = nums[y]
			k += 2
		}
		k = 1
		for x := 0; x < lettersCount; x++ {
			res[k] = letters[x]
			k += 2
		}
	}
	return string(res)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := reformat(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
