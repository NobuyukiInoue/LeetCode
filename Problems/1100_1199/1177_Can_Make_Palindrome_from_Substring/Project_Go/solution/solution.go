package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canMakePaliQueries(s string, queries [][]int) []bool {
	// 192ms
	sLen := len(s)
	results := []bool {}
	masks := make([]int, sLen + 1)

	j, mask := 0, 0
	for i := 0 ; i < sLen; i++ {
		mask ^= (1 << (s[i] - 'a'))
		j++
		masks[j] = mask
	}

	for _, query := range queries {
		if query[2] >= 13 {
			results = append(results, true)
		} else {
			results = append(results, bitCount(masks[query[1] + 1] ^ masks[query[0]]) /2 <= query[2])
		}
	}

	return results
}

func bitCount(i int) int {
	i = i - ((i >> 1) & 0x55555555)
	i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
	i = (i + (i >> 4)) & 0x0f0f0f0f
	i = i + (i >> 8)
	i = i + (i >> 16)
	return i & 0x3f
}

func BoolArrayToString(res []bool) string {
	if len(res) <= 0 {
		return ""
	}

	resultStr := strconv.FormatBool(res[0])
	for i := 1; i < len(res); i++ {
		resultStr += ", " + strconv.FormatBool(res[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[")

	s := strings.Replace(flds[0], "[[", "", -1)
	str_queries := strings.Split(strings.Replace(flds[1], "]]]", "", -1), "],[")
	queries := make([][]int, len(str_queries))
	for i := 0; i < len(str_queries); i++ {
		queries[i] = StringToIntArray(str_queries[i])
	}
	fmt.Printf("queries = %s\n", IntIntArrayToGridString(queries))

	timeStart := time.Now()

	result := canMakePaliQueries(s, queries)

	timeEnd := time.Now()

	fmt.Printf("resut = %s\n",BoolArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
