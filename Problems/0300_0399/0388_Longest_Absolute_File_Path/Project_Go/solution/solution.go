package solution

import (
	"fmt"
	"strings"
	"time"
)

func lengthLongestPath(input string) int {
    ss := strings.Split(input, "\n")
    var max int
    segLen := make(map[int]int)
    for _, str := range ss {
        curIndent := getIndent(str)
        name := str[curIndent:]
        if strings.Contains(name, ".") {
            curLen := len(name)
            for i := curIndent-1; i >= 0; i-- {
                curLen += segLen[i] + 1
            }
            if curLen > max {
                max = curLen
            }
        } else {
            segLen[curIndent] = len(name)
        }
    }
    return max
}

func getIndent(str string) int {
    var ret int
    for i := 0; i < len(str); i++ {
        if str[i] != '\t' {
            break
        }
        ret++
    }
    return ret
}

/*
func lengthLongestPath(input string) int {
	paths := strings.Split(input, "\\n")
	stack := make([]int, len(paths)+1)
	maxLen := 0
	for _, s := range paths {
		lev := strings.LastIndex(s, "\t") + 1
		stack[lev+1] = stack[lev] + len(s) - lev + 1
		curLen := stack[lev+1]
		if strings.Index(s, ".") >= 0 {
			maxLen = max(maxLen, curLen-1)
		}
	}
	return maxLen
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	input := strings.Replace(temp, "]", "", -1)

	fmt.Printf("input = %s\n", input)

	timeStart := time.Now()

	result := lengthLongestPath(input)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
