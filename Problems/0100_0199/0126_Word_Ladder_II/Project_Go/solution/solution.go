package solution

import (
	"fmt"
	"strings"
	"time"
)

// 144ms
type item struct {
	word string
	path []string
}

func findLadders(beginWord string, endWord string, wordList []string) [][]string {
	_, find := find(wordList, endWord)
	if !find || len(beginWord) == 0 || len(endWord) == 0 {
		return make([][]string, 0)
	}

	n := len(beginWord)
	combo := make(map[string][]string)
	for _, w := range wordList {
		for i := 0; i < n; i++ {
			iterWord := w[:i] + "*" + w[i+1:]
			combo[iterWord] = append(combo[iterWord], w)
		}
	}

	queue := make([]item, 0)
	queue = append(queue, item{beginWord, []string{beginWord}})
	visited := make(map[string]bool)
	visited[beginWord] = true

	res := make([][]string, 0)
	for len(queue) > 0 {
		k := len(queue)
		nextLayterVisited := make(map[string]bool)
		for i := 0; i < k; i++ {
			pop := queue[0]
			currWord := pop.word
			path := pop.path

			if currWord == endWord {
				res = append(res, path)
			}

			for j := 0; j < n; j++ {
				iterWord := currWord[:j] + "*" + currWord[j+1:]
				_, ok := combo[iterWord]
				if ok {
					nextWords := combo[iterWord]
					for _, nextWord := range nextWords {
						_, isVisited := visited[nextWord]
						if !isVisited {
							var newPath = make([]string, len(path))
							copy(newPath, path)
							newPath = append(newPath, nextWord)
							queue = append(queue, item{nextWord, newPath})
							nextLayterVisited[nextWord] = true
						}
					}
				}
			}
			queue = queue[1:]
		}
		if len(res) > 0 {
			return res
		}
		for key, _ := range nextLayterVisited {
			visited[key] = true
		}
	}

	return res
}

func find(slice []string, val string) (int, bool) {
	for i, item := range slice {
		if item == val {
			return i, true
		}
	}
	return -1, false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	beginWord := flds[0]
	endWord := flds[1]
	wordList := strings.Split(flds[2], ",")
	fmt.Printf("beginWord = %s\n", beginWord)
	fmt.Printf("endWord   = %s\n", endWord)
	fmt.Printf("wordList  = %s\n", wordList)

	timeStart := time.Now()

	result := findLadders(beginWord, endWord, wordList)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
