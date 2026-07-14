class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS
            ):
                return

            ch = board[r][c]

            if ch == "#" or ch not in node.children:
                return

            nxt = node.children[ch]

            if nxt.word:
                res.append(nxt.word)
                nxt.word = None   # avoid duplicates

            board[r][c] = "#"

            dfs(r + 1, c, nxt)
            dfs(r - 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)

            board[r][c] = ch

            # Prune Trie
            if not nxt.children:
                del node.children[ch]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res