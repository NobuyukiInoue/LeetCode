package solution

import (
	"fmt"
	"strings"
	"time"
)

func modifyString(s string) string {
    // 0ms
    res := []rune(s)
    for i := 0; i < len(res); i++ {
        if res[i] == '?' {
            for _, ch := range("abc") {
                if i > 0 && res[i - 1] == ch {
                    continue
                }
                if i + 1 < len(res) && res[i + 1] == ch {
                    continue
                }
                res[i] = ch
                break
            }
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

	result := modifyString(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
