class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        inital = Trie()
        visit = set()
        for i in words:
            inital.insert(i)        
        ROW, COL = len(board), len(board[0])

        def dfs(r,c,node, word):

            if c < 0 or r < 0 or ROW <= r or c >= COL or (r,c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            node = node.children[(board[r][c])]
            word += board[r][c]
            if node.end:
                result.add(word)
            dfs(r - 1,c,node,word)
            dfs(r + 1,c,node,word)
            dfs(r,c + 1,node,word)
            dfs(r,c - 1,node,word)
            visit.remove((r,c))
        for i in range(ROW):
            for j in range(COL):
                dfs(i,j,inital.root,"")
        return list(result)