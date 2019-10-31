package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func restoreIpAddresses(s string) []string {
	// 0ms
	var buffer []rune
	var res []string
	helper(s, 0, 1, buffer, &res)
	return res
}

func helper(s string, i, l int, buffer []rune, res *[]string) {
	n := len(s)
	if l > 4 {
		if i == n {
			buffer = buffer[:len(buffer)-1]
			cur := make([]rune, len(buffer))
			copy(cur, buffer)
			*res = append(*res, string(cur))
		}
		return
	}
	var num int
	if i < n && s[i] == '0' {
		buffer = append(buffer, '0', '.')
		helper(s, i+1, l+1, buffer, res)
	} else {
		for j := i; j < i+3 && j < n; j++ {
			num = 10*num + int(s[j]-'0')
			if num <= 255 {
				buffer = append(buffer, []rune(s[i:j+1])...)
				buffer = append(buffer, '.')
				helper(s, j+1, l+1, buffer, res)
				buffer = buffer[:len(buffer)-(j-i+1)-1]
			}
		}
	}
}

func restoreIpAddresses2(s string) []string {
	// 0ms
	var validateArr []string
	for i1 := 1; i1 <= len(s)-3 && i1 < 4; i1++ {
		for i2 := i1 + 1; i2 <= len(s)-2 && i2-i1 < 4; i2++ {
			for i3 := i2 + 1; i3 <= len(s)-1 && i3-i2 < 4; i3++ {
				if (len(s[0:i1]) > 1 && s[0:i1][0:1] == "0") || (len(s[i1:i2]) > 1 && s[i1:i2][0:1] == "0") ||
					(len(s[i2:i3]) > 1 && s[i2:i3][0:1] == "0") || (len(s[i3:]) > 1 && s[i3:][0:1] == "0") {
					continue
				}
				intTmp1, _ := strconv.Atoi(s[0:i1])
				intTmp2, _ := strconv.Atoi(s[i1:i2])
				intTmp3, _ := strconv.Atoi(s[i2:i3])
				intTmp4, _ := strconv.Atoi(s[i3:])
				if intTmp1 < 256 && intTmp2 < 256 && intTmp3 < 256 && intTmp4 < 256 {
					validateArr = append(validateArr, s[0:i1]+"."+s[i1:i2]+"."+s[i2:i3]+"."+s[i3:])
				}
			}
		}
	}
	return validateArr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = [%s]\n", s)
	timeStart := time.Now()

	result := restoreIpAddresses(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
