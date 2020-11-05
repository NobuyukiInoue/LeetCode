package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func alertNames(keyName []string, keyTime []string) []string {
	// 164ms
	nameToTime := map[string][]int{}
	for i, name := range(keyName) {
		hourMinutes := minute(keyTime[i])
		nameToTime[name] = append(nameToTime[name], hourMinutes)
	}
	names := []string{}
	for k, v := range(nameToTime) {
		if checkWarning(v) {
			names = append(names, k)
		}
	}
	sort.Strings(names)
	return names
}

func minute(timeStr string) int {
	flds := strings.Split(timeStr, ":")
	hour, _ := strconv.Atoi(flds[0])
	min, _  := strconv.Atoi(flds[1])
	return hour*60 + min
}

func checkWarning(minutes []int) bool {
	sort.Ints(minutes)
	for i := 2; i < len(minutes); i++ {
		diff := minutes[i] - minutes[i - 2]
		if diff <= 60 {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)

	flds := strings.Split(temp, "],[")
	keyName := strings.Split((strings.Replace(flds[0], "[[", "", -1)), ",")
	keyTime := strings.Split((strings.Replace(flds[1], "]]", "", -1)), ",")

	fmt.Printf("keyName = %s\n", StringArrayToString(keyName))
	fmt.Printf("keyTime = %s\n", StringArrayToString(keyTime))

	timeStart := time.Now()

	result := alertNames(keyName, keyTime)

	timeEnd := time.Now()
	fmt.Printf("result =  %s\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
