package solution

import (
	"fmt"
	"strings"
	"time"
)

func shiftingLetters(s string, shifts []int) string {
	// 20ms
	acum := 0
	ans := make([]byte, len(s))
	for i := len(s) - 1; i >= 0; i-- {
		acum = (acum + shifts[i]) % 26
		ans[i] = 97 + (s[i]+byte(acum)-97)%26
	}
	return string(ans)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s := flds[0]
	shifts := StringToIntArray(flds[1])
	fmt.Printf("s = %s\n", s)
	fmt.Printf("shifts = %s\n", IntArrayToString(shifts))

	timeStart := time.Now()

	result := shiftingLetters(s, shifts)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
