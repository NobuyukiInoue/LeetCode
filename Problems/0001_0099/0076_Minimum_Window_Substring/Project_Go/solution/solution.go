package solution

import (
	"fmt"
	"strings"
	"time"
)

func minWindow(s string, t string) string {
	// 0ms
	if len(s) < len(t) {
		return ""
	}

	need := make([]int, 52)
	totalNeed := 0
	have := make([]int, 52)

	for i := range t {
		idx := charToIdx(t[i])
		
		need[idx]++
		totalNeed++
	}

	ans := ""
	ansLen := maxInt
	i := 0
	for j := range s {
		idx := charToIdx(s[j])
		if have[idx] < need[idx] {
			totalNeed--
		}
		have[idx]++
		if totalNeed == 0 {
			for i <= j {
				iidx := charToIdx(s[i])
				if need[iidx] > 0 {
					if j - i + 1 < ansLen {
						ansLen = j - i + 1
						ans = s[i:j+1]
					}
					if have[iidx]-1 >= need[iidx] {
						have[iidx]--
					} else {
						break
					}
				}
				i++
			}
		}
	}
	
	return ans
}

func charToIdx(c byte) int {
	if c <= 'Z' {
		return int(c - 'A')
	}
	
	return int(c - 'a' + 26)
}

const maxUint = ^uint(0)		 // 1111...1
const minUint = uint(0)		  // 0000...0
const maxInt = int(maxUint >> 1) // 0111...1
const minInt = -maxInt - 1	   // 1000...0

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	s, t := flds[0], flds[1]
	fmt.Printf("s = %s, t = %s\n", s, t)

	timeStart := time.Now()

	result := minWindow(s, t)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
