package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func numberOfRounds(loginTime string, logoutTime string) int {
	// 0ms
	ts_hh, _ := strconv.Atoi(loginTime[0:2])
	tf_hh, _ := strconv.Atoi(logoutTime[0:2])
	ts_mm, _ := strconv.Atoi(loginTime[3:])
	tf_mm, _ := strconv.Atoi(logoutTime[3:])
	ts := 60*ts_hh + ts_mm
	tf := 60*tf_hh + tf_mm
	if 0 <= tf-ts && tf-ts < 15 {
		return 0
	}
	if ts > tf {
		return tf/15 - (ts+14)/15 + 96
	}
	return tf/15 - (ts+14)/15
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	loginTime := flds[0]
	logoutTime := flds[1]
	fmt.Printf("loginTime = %s, logoutTime = %s\n", loginTime, logoutTime)

	timeStart := time.Now()

	result := numberOfRounds(loginTime, logoutTime)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
