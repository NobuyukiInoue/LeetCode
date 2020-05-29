package trie

// 56ms

type Trie struct {
	letters [26]*Trie
	isWord  bool
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{[26]*Trie{}, false}
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {

	node := this

	for i, _ := range word {

		letter := word[i]
		index := letter - 'a'

		if node.letters[index] == nil {
			node.letters[index] = &Trie{[26]*Trie{}, false}
		}

		node = node.letters[index]
	}

	node.isWord = true
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	return this.searchOrStartsWith(word, false)
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	return this.searchOrStartsWith(prefix, true)
}

func (this *Trie) searchOrStartsWith(word string, startsWith bool) bool {
	node := this

	for i, _ := range word {

		letter := word[i]
		index := letter - 'a'

		if node.letters[index] == nil {
			return false
		}

		node = node.letters[index]
	}

	return startsWith || node.isWord
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
