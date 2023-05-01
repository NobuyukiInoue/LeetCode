package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func pyramidTransition(bottom string, allowed []string) bool {
	// 631ms - 664ms
	nexts := map[string][]byte{}
	for _, v := range allowed {
		nexts[v[:2]] = append(nexts[v[:2]], v[2])
	}

	var dfs func(cur, next []byte) bool
	dfs = func(cur, next []byte) bool {
		if len(cur) == 1 {
			return true
		}
		if len(cur) == len(next)+1 {
			return dfs(next, nil)
		}
		i := len(next)
		s := string(cur[i : i+2])
		for _, c := range nexts[s] {
			if dfs(cur, append(next, c)) {
				return true
			}
		}
		return false
	}

	return dfs([]byte(bottom), nil)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	bottom := flds[0]
	allowed := strings.Split(flds[1], ",")
	fmt.Printf("bottom = %s, allowed = %s\n", bottom, StringArrayToString(allowed))

	timeStart := time.Now()

	result := pyramidTransition(bottom, allowed)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
