class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False 

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word: 
            if c not in cur.children: 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True 

    def search(self, word: str) -> bool:
        cur = self.root
        idx = 0
        while idx < len(word): 
            if word[idx] not in cur.children: 
                return False 
            cur = cur.children[word[idx]]
            idx += 1
        if not cur.end: 
            return False
        return True     

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        idx = 0 
        while idx < len(prefix): 
            if prefix[idx] not in cur.children:
                return False 
            cur = cur.children[prefix[idx]]
            idx += 1
        return True 

        