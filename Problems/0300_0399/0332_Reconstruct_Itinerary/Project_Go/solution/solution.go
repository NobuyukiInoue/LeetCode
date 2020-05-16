package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func findItinerary(tickets [][]string) []string {
	hash := map[string][]string{}
	hash2 := map[string][]bool{}
	for _, tkt := range tickets {
		hash[tkt[0]] = append(hash[tkt[0]], tkt[1])
		hash2[tkt[0]] = append(hash2[tkt[0]], false)
	}
	for _, v := range hash {
		sort.Strings(v)
	}
	current := "JFK"
	travel := []string{"JFK"}
	dfs(current, len(tickets), hash, hash2, &travel)
	return travel
}

func dfs(current string, left int, hash map[string][]string, hash2 map[string][]bool, travel *[]string) bool {
	if left == 0 {
		return true
	}
	if len(hash[current]) == 0 {
		return false
	}
	for i, v := range hash2[current] {
		if v == false {
			hash2[current][i] = true
			*travel = append(*travel, hash[current][i])
			if dfs(hash[current][i], left-1, hash, hash2, travel) == true {
				return true
			}
			hash2[current][i] = false
			*travel = (*travel)[:len(*travel)-1]
		}
	}
	return false
}

func strArrayToString(data []string) string {
	if len(data) <= 0 {
		return ""
	}

	res := "[" + data[0]
	for i := 1; i < len(data); i++ {
		res += ", \"" + data[i] + "\""
	}

	return res + "]"
}

func strArrayArrayToString(data [][]string) string {
	if len(data) <= 0 {
		return ""
	}

	res := strArrayToString(data[0])
	for i := 1; i < len(data); i++ {
		res += ", " + strArrayToString(data[i])
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)
	data := strings.Split(flds, "],[")

	tickets := make([][]string, len(data))
	for i := 0; i < len(data); i++ {
		tickets[i] = strings.Split(data[i], ",")
	}

	fmt.Printf("tickets = [%s]\n", strArrayArrayToString(tickets))
	timeStart := time.Now()

	result := findItinerary(tickets)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", strArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
