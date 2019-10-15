package solution

import (
	"bytes"
	"fmt"
	"strings"
	"time"
)

func reverseWords(s string) string {
	var words = strings.Split(s, " ")
	var buf bytes.Buffer
	var length = len(words)
	for i := 0; i < length; i++ {
		for j := len(words[i]) - 1; j >= 0; j-- {
			buf.WriteByte(words[i][j])
		}
		buf.WriteString(" ")
	}
	var result = buf.String()
	return strings.Trim(result, " ")
}

func reverseWords_work(s string) string {
	ca := strings.Split(s, "")
	for i := 0; i < len(ca); i++ {
		if ca[i] != " " && ca[i] != "," {
			j := i
			for j+1 < len(ca) && ca[j+1] != " " && ca[j+1] != "," {
				j++
			}

			//ca = reverse(ca, i, j)
			for ii, jj := i, j; ii < jj; ii, jj = ii+1, jj-1 {
				ca[ii], ca[jj] = ca[jj], ca[ii]
			}
			i = j
		}
	}
	return strings.Join(ca, "")
}

/*
func reverse(ca string, i int, j int) string {
	reverseStr := []rune(ca)
	for ; i < j; i, j = i+1, j-1 {
		reverseStr[i], reverseStr[j] = reverseStr[j], reverseStr[i]
	}

	return string(reverseStr)
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := reverseWords(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
