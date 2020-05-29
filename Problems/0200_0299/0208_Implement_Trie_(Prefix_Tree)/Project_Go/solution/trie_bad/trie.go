package trie

import "./trienode"

type Trie struct {
	root      trienode.TrieNode
	startWith bool
}

/** Initialize your data structure here. */
func Constructor() Trie {
	trie := new(Trie)
	trie.root = trienode.Constructor()
	return *trie
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	insert2(word, this.root, 0)
}

func insert2(word string, node trienode.TrieNode, idx int) {
	if idx == len(word) {
		node.IsWord = true
		return
	}

	index := word[idx] - 'a'

	//	if node.Children[index] == nil {
	if node.IsExistChildren[index] == false {
		node.Children[index] = trienode.Constructor()
		node.IsExistChildren[index] = true
	}

	insert2(word, node.Children[index], idx+1)
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	return this.Search2(word, this.root, 0)
}

func (this *Trie) Search2(word string, node trienode.TrieNode, idx int) bool {
	if idx == len(word) {
		this.startWith = true
		return node.IsWord
	}

	index := word[idx] - 'a'

	if node.IsExistChildren == nil {
		this.startWith = false
		return false
	}

	if node.IsExistChildren[index] == false {
		this.startWith = false
		return false
	}

	return this.Search2(word, this.root.Children[index], idx+1)
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	this.Search(prefix)
	return this.startWith
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
