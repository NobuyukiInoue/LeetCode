package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func accountsMerge(accounts [][]string) [][]string {
	// 88ms
	result := make([][]string, 0)
	graph, reverseIndex := buildGraph(accounts)

	visited := make(map[string]bool)

	for key := range graph {

		if _, ok := visited[key]; ok {
			continue
		}
		visited[key] = true
		emails := make([]string, 0)
		dfs(&graph, key, &visited, &emails)
		sort.Strings(emails)
		emails = append([]string{reverseIndex[key]}, emails...)
		result = append(result, emails)
	}
	return result
}

func dfs(graph *map[string]map[string]bool, key string, visited *map[string]bool, emails *[]string) {
	*emails = append(*emails, key)
	for neighbor := range (*graph)[key] {

		if _, ok := (*visited)[neighbor]; ok {
			continue
		}
		(*visited)[neighbor] = true
		dfs(graph, neighbor, visited, emails)
	}
}

func buildGraph(accounts [][]string) (map[string]map[string]bool, map[string]string) {
	graph := make(map[string]map[string]bool) // email -> neighbor nodes
	reverseIndex := make(map[string]string)
	for _, account := range accounts {
		for i, s := range account {
			if i == 0 {
				continue
			}
			reverseIndex[s] = account[0]
			if _, ok := graph[s]; !ok {
				graph[s] = make(map[string]bool)
			}
			if i > 1 {
				graph[account[i-1]][s] = true
				graph[s][account[i-1]] = true
			}
		}
	}
	return graph, reverseIndex
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	accounts := make([][]string, len(flds))
	for i := 0; i < len(accounts); i++ {
		accounts[i] = strings.Split(flds[i], ",")
	}

	fmt.Printf("accounts = %s\n", accounts)

	timeStart := time.Now()

	result := accountsMerge(accounts)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
