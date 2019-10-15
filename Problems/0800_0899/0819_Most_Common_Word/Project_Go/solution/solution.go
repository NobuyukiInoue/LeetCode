package solution

import (
	"fmt"
	"strings"
	"time"
)

func mostCommonWord(paragraph string, banned []string) string {
	targetStr := strings.Replace(paragraph, ", ", ",", -1)
	targetStr = strings.Replace(targetStr, ",", " ", -1)

	replaceChar := []string{"'", ";", ".", "?", "!"}
	for _, rWord := range replaceChar {
		targetStr = strings.Replace(targetStr, rWord, "", -1)
	}

	for _, rWord := range banned {
		targetStr = strings.Replace(targetStr, " "+rWord, "", -1)
	}

	targetStrArr := strings.Split(targetStr, " ")
	dic := make(map[string]int, 0)
	max, tKey := 0, ""

	for _, cur := range targetStrArr {
		cur = strings.ToLower(cur)

		hit := false
		for _, tBanned := range banned {
			if cur == tBanned {
				hit = true
				break
			}
		}

		if hit {
			continue
		}

		_, exists := dic[cur]
		if exists {
			dic[cur]++
		} else {
			dic[cur] = 1
		}

		if dic[cur] > max {
			tKey, max = cur, dic[cur]
		}
	}

	return tKey
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	paragraph := flds[0]
	banned := strings.Split(flds[1], ",")

	fmt.Printf("paragraph = %s\n", paragraph)
	fmt.Printf("banned[] = %s\n", banned)

	timeStart := time.Now()

	result := mostCommonWord(paragraph, banned)
	fmt.Printf("result = %s\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
