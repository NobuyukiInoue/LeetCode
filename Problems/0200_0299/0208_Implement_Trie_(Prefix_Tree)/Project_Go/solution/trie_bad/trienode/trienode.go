package trienode

type TrieNode struct {
	Children        []TrieNode
	IsExistChildren []bool
	IsWord          bool
}

/** Initialize your data structure here. */
func Constructor() TrieNode {
	trienode := new(TrieNode)
	trienode.Children = make([]TrieNode, 26)
	trienode.IsExistChildren = make([]bool, 26)
	for i := 0; i < len(trienode.IsExistChildren); i++ {
		trienode.IsExistChildren[i] = false
	}
	return *trienode
}
