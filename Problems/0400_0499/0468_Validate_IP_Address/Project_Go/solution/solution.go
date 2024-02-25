package solution

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"time"
)

// 0ms - 1ms
func validIPAddress(queryIP string) string {
	flds_ipv4 := strings.Split(queryIP, ".")
	flds_ipv6 := strings.Split(queryIP, ":")
	if len(flds_ipv4) == 4 {
		for _, s := range flds_ipv4 {
			if !isIPv4(s) {
				return "Neither"
			}
		}
		return "IPv4"
	} else if len(flds_ipv6) == 8 {
		for _, s := range flds_ipv6 {
			if !isIPv6(s) {
				return "Neither"
			}
		}
		return "IPv6"
	} else {
		return "Neither"
	}
}

func isIPv4(s string) bool {
	s_int, error := strconv.Atoi(s)
	if error != nil {
		return false
	}
	return strconv.Itoa(s_int) == s && 0 <= s_int && s_int <= 255
}

func isIPv6(s string) bool {
	s_int, error := strconv.ParseInt(s, 16, 64)
	if error != nil {
		return false
	}
	return len(s) <= 4 && s_int >= 0
}

// 0ms
const i8 string = `([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])`

var ipv4 = regexp.MustCompile("^" + i8 + `(\.` + i8 + `){3}$`)

const hex string = "[0-9a-f]{1,4}"

var ipv6 = regexp.MustCompile("^(?i)[1-9a-f][0-9a-f]{0,3}(:" + hex + "){7}$")

func validIPAddress2(queryIP string) string {
	if ipv4.Match([]byte(queryIP)) {
		return "IPv4"
	}

	if ipv6.Match([]byte(queryIP)) {
		return "IPv6"
	}
	return "Neither"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	queryIP := strings.Replace(temp, "]", "", -1)
	fmt.Printf("queryIP = \"%s\"\n", queryIP)

	timeStart := time.Now()

	result := validIPAddress(queryIP)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
