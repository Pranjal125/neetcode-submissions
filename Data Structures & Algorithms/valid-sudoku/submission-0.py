class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue                      # skip empty cells

                box = (r // 3, c // 3)

                # duplicate in this row, column, or box?
                if (val in rows.get(r, set()) or
                    val in cols.get(c, set()) or
                    val in boxes.get(box, set())):
                    return False

                # record it in all three jars
                rows.setdefault(r, set()).add(val)
                cols.setdefault(c, set()).add(val)
                boxes.setdefault(box, set()).add(val)

        return True       # scanned everything, no duplicates → valid