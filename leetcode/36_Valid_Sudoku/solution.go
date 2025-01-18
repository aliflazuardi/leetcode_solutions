package solution

func isValidSudoku(board [][]byte) bool {
	rows := make(map[int]field)
	cols := make(map[int]field)
	squares := make(map[int]field)

	for i := 0; i < 9; i++ {
		rows[i] = make(map[byte]bool)
		for j := 0; j < 9; j++ {
			if cols[j] == nil {
				cols[j] = make(map[byte]bool)
			}
			if squares[(3*(i/3))+j/3] == nil {
				squares[(3*(i/3))+j/3] = make(map[byte]bool)
			}

			if board[i][j] == '.' {
				continue
			}

			if rows[i][board[i][j]] || cols[j][board[i][j]] || squares[(3*(i/3))+j/3][board[i][j]] {
				return false
			}

			rows[i][board[i][j]] = true
			cols[j][board[i][j]] = true
			squares[(3*(i/3))+j/3][board[i][j]] = true
		}
	}

	return true
}

type field map[byte]bool
