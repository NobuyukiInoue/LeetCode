package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"

	"./worddictionary"
)

func WordDictionaryMain(ope []string, words []string) {
	if len(ope) != len(words) {
		return
	}
	if len(ope) <= 0 || len(words) <= 0 {
		return
	}

	WordDictionary := worddictionary.Constructor()
	for i, _ := range ope {
		if ope[i] == "addWord" {
			WordDictionary.AddWord(words[i])
			fmt.Printf("addWord(%s)\n", words[i])

		} else if ope[i] == "search" {
			res := WordDictionary.Search(words[i])
			fmt.Printf("search(%s) ... %s\n", words[i], strconv.FormatBool(res))
		}
	}
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

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[")

	flds0 := strings.Replace(flds[0], "[", "", -1)
	flds0 = strings.Replace(flds0, "[", "", -1)
	flds0 = strings.Replace(flds0, "]", "", -1)
	ope := strings.Split(flds0, ",")

	flds1 := strings.Replace(flds[1], "]]", "", -1)
	words := strings.Split(flds1, "],[")

	fmt.Printf("ope = %s\n", strArrayToString(ope))
	fmt.Printf("words = %s\n", strArrayToString(words))

	timeStart := time.Now()

	WordDictionaryMain(ope, words)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
