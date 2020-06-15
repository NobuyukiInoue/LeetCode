package solution

import (
	"fmt"
	"strings"
	"time"
)

func simplifyPath(path string) string {
	// 0ms
	stack := make([]string, 0)
	flds := strings.Split(path, "/")

	for _, fld := range flds {
		if fld == "" || fld == "." {
			continue
		} else if fld == ".." {
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
		} else {
			stack = append(stack, fld)
		}
	}

	res := "/"
	for i := 0; i < len(stack); i++ {
		res += stack[i] + "/"
	}

	if len(res) <= 1 {
		return "/"
	}
	return res[:len(res)-1]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	path := strings.Replace(temp, "]", "", -1)
	fmt.Printf("path = %s\n", path)

	timeStart := time.Now()

	result := simplifyPath(path)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
