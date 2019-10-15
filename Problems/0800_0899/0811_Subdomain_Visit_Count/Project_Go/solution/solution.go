package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func subdomainVisits(cpdomains []string) []string {
	if len(cpdomains) <= 0 {
		return []string{}
	}

	dic := make(map[string]int, 0)
	for i := range cpdomains {
		flds := strings.Split(cpdomains[i], " ")
		count, _ := strconv.Atoi(flds[0])
		domain := flds[1]

		pos := 0
		for true {
			value, exists := dic[domain]
			if exists {
				dic[domain] = value + count
			} else {
				dic[domain] = count
			}

			pos = strings.Index(domain, ".")
			if pos >= 0 {
				domain = domain[pos+1:]
			} else {
				break
			}
		}
	}

	result := make([]string, len(dic))

	i := 0
	for key, value := range dic {
		result[i] = strconv.Itoa(value) + " " + key
		i++
	}

	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)

	cpdomains := strings.Split(temp, ",")

	fmt.Printf("cpdomains = %s\n", cpdomains)

	timeStart := time.Now()

	result := subdomainVisits(cpdomains)
	fmt.Printf("result = %s\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
