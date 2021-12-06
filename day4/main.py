# parse input
def parse_input():
    lines = []
    with open("input.txt") as f:
        for l in f:
            lines.append(l.strip())

    drawn_numbers = [int(x) for x in lines[0].split(",")]

    boards = []

    for i in range(2, len(lines), 6):
        board = []
        for n in range(5):
            board.append([int(x) for x in lines[i + n].split(" ") if x != ""])
        boards.append(board)
    return drawn_numbers, boards

drawn_numbers, boards = parse_input()

won = set()
for num in drawn_numbers:
    # altra sintassi per il nested loop
    '''for board, row, coloumn in ((board, row, coloumn)
                                for board in set(range(len(boards))) - won
                                for row in range(5)
                                for coloumn in range(5)
                                if boards[board][row][coloumn] == num):'''
    for board in set(range(len(boards))) - won: # ad ogni iterazione toglie dal set delle board quelli che hanno gia vinto
        for row in range(5):
            for coloumn in range(5):
                if boards[board][row][coloumn] == num:
                    boards[board][row][coloumn] = -1
                    if(sum(boards[board][row]) == -5 or sum(row[coloumn] for row in boards[board]) == -5):
                        won.add(board)
                        if len(won)== 1: # parte 1, primo board che vince = quando il set won ha dimensione 1
                            print('Part 1', sum(sum(c for c in row if c > 0) for row in boards[board])*num)
                        if len(won) == len(boards):
                            print('Part 2', sum(sum(c for c in row if c > 0) for row in boards[board])*num)
