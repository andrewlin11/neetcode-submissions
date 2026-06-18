class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == ".":
                    continue
                if (col in boxes[i // 3, j // 3]) or (col in rows[i]) or (col in cols[j]):
                    return False
                boxes[i // 3, j // 3].add(col)
                rows[i].add(col)
                cols[j].add(col)
        return True
