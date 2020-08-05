package solution

import (
	"fmt"
	"strings"
	"time"
)

func restoreString(s string, indices []int) string {
	// 4ms
	res := make([]rune, len(s))
	for i := 0; i < len(indices); i++ {
		res[indices[i]] = rune(s[i])
	}
	return string(res)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s := flds[0]
	indices := StringToIntArray(flds[1])
	fmt.Printf("s = %s, indices = [%s]\n", s, IntArrayToString(indices))

	timeStart := time.Now()

	result := restoreString(s, indices)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
