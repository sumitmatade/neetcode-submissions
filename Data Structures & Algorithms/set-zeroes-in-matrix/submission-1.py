class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False  # Track if the first row needs to be zeroed

        # Step 1: Mark rows and columns that need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # Mark column header
                    if r > 0:
                        matrix[r][0] = 0  # Mark row header
                    else:
                        rowZero = True

        # Step 2: Zero out cells based on marks (excluding 1st row & 1st col)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Step 3: Zero out the first column if needed
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Step 4: Zero out the first row if needed
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0