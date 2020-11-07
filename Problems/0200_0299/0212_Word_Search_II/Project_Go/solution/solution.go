package solution

import (
	"fmt"
	"strings"
	"time"
)

type TrieNode struct {
	word     string
	children [26]*TrieNode
}

func findWords(board [][]byte, words []string) []string {
	// 24ms
	root := &TrieNode{}
	for _, w := range words {
		node := root
		for _, c := range w {
			if node.children[c-'a'] == nil {
				node.children[c-'a'] = &TrieNode{}
			}
			node = node.children[c-'a']
		}
		node.word = w
	}

	result := make([]string, 0)
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			dfs(i, j, board, root, &result)
		}
	}
	return result
}

func dfs(i, j int, board [][]byte, node *TrieNode, result *[]string) {
	if i < 0 || j < 0 || i == len(board) || j == len(board[0]) {
		return
	}
	c := board[i][j]
	if c == '#' || node.children[c-'a'] == nil {
		return
	}
	node = node.children[c-'a']
	if node.word != "" {
		*result = append(*result, node.word)
		node.word = ""
	}

	board[i][j] = '#'
	dfs(i+1, j, board, node, result)
	dfs(i-1, j, board, node, result)
	dfs(i, j+1, board, node, result)
	dfs(i, j-1, board, node, result)
	board[i][j] = c
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "]],[")

	str_board := strings.Split(strings.Replace(flds[0], "[[[", "", -1), "],[")
	board := make([][]byte, len(str_board))
	for i := 0; i < len(str_board); i++ {
		board[i] = StringToByteArray(strings.Replace(str_board[i], ",", "", -1))
	}
	fmt.Printf("board = %s\n", ByteByteArrayToGridString(board))

	words := strings.Split(strings.Replace(flds[1], "]]", "", -1), ",")
	fmt.Printf("words = %s\n", words)

	timeStart := time.Now()

	result := findWords(board, words)

	timeEnd := time.Now()

	fmt.Printf("board = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
