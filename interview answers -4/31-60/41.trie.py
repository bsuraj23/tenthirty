#41.Implement a Trie in Python.
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

print(trie.search("apple"))  # True
print(trie.search("app"))    # True
print(trie.search("ap"))     # False
print(trie.starts_with("ap")) # True
print(trie.starts_with("ban")) # True
print(trie.search("banana"))  # True
print(trie.search("band"))    # False
