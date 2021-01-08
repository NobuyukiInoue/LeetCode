package solution

import (
	"bytes"
	"fmt"
	"strconv"
	"strings"
	"time"
)

func originalDigits(s string) string {
	// 4ms
	counter := [26]int{}
	for _, v := range s {
		counter[v-'a']++
	}
	numberCounter := [10]int{}
	numberCounter[0] = counter['z'-'a'] // zero - z
	numberCounter[2] = counter['w'-'a'] // two - w
	numberCounter[4] = counter['u'-'a'] // four - u
	numberCounter[6] = counter['x'-'a'] // six - x
	numberCounter[8] = counter['g'-'a'] // eight - g

	numberCounter[3] = counter['h'-'a'] - numberCounter[8]                                       // eight & three - h
	numberCounter[5] = counter['f'-'a'] - numberCounter[4]                                       // four & five - f
	numberCounter[7] = counter['v'-'a'] - numberCounter[5]                                       // five & seven - v
	numberCounter[1] = counter['o'-'a'] - numberCounter[0] - numberCounter[2] - numberCounter[4] // zero & one & two & four - o
	numberCounter[9] = counter['i'-'a'] - numberCounter[5] - numberCounter[6] - numberCounter[8] // five & six & eight & nine - i
	bb := bytes.Buffer{}
	for i := 0; i <= 9; i++ {
		for j := 0; j < numberCounter[i]; j++ {
			_ = bb.WriteByte('0' + byte(i))
		}
	}
	return bb.String()
}

func originalDigits2(s string) string {
	// 56ms
	var count [10]int

	for i := 0; i < len(s); i++ {
		c := s[i]
		if c == 'z' {
			count[0]++
		}
		if c == 'w' {
			count[2]++
		}
		if c == 'x' {
			count[6]++
		}
		if c == 's' {
			count[7]++ //7-6
		}
		if c == 'g' {
			count[8]++
		}
		if c == 'u' {
			count[4]++
		}
		if c == 'f' {
			count[5]++ //5-4
		}
		if c == 'h' {
			count[3]++ //3-8
		}
		if c == 'i' {
			count[9]++ //9-8-5-6
		}
		if c == 'o' {
			count[1]++ //1-0-2-4
		}
	}
	count[7] -= count[6]
	count[5] -= count[4]
	count[3] -= count[8]
	count[9] = count[9] - count[8] - count[5] - count[6]
	count[1] = count[1] - count[0] - count[2] - count[4]

	res := ""
	for i := 0; i <= 9; i++ {
		for j := 0; j < count[i]; j++ {
			res += strconv.Itoa(i)
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := originalDigits(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
