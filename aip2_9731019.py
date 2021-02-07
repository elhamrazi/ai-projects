import copy


class Board:
    def __init__(self, dim):
        self.dim = dim
        self.board = {}
        self.mrv = {}

    def update_domain(self, chosen, value):
        global colors
        i = chosen[0]
        j = chosen[1]
        color = colors[value[1]]
        for k in range(self.dim):
            x = copy.deepcopy(self.board[(i, k)])
            for v in x:
                if v[0] == value[0]:
                    self.board[(i, k)].remove(v)
            self.mrv[(i, k)] = len(self.board[(i, k)])
            y = self.board[(k, j)]
            for v in y:
                if v[0] == value[0]:
                    self.board[(k, j)].remove(v)
            self.mrv[(k, j)] = len(self.board[(k, j)])

        if i > 0:
            x = copy.deepcopy(self.board[(i-1, j)])
            for v in x:
                cv = colors[v[1]]
                if v[1] == value[1]:
                    self.board[(i-1, j)].remove(v)
                if value[0] > v[0]:
                    if cv > color:
                        self.board[(i-1, j)].remove(v)

        if i < self.dim-1:
            x = copy.deepcopy(self.board[(i+1, j)])
            for v in x:
                cv = colors[v[1]]
                if v[1] == value[1]:
                    self.board[(i+1, j)].remove(v)
                if value[0] > v[0]:
                    if cv > color:
                        self.board[(i+1, j)].remove(v)

        if j > 0:
            x = copy.deepcopy(self.board[(i, j-1)])
            for v in x:
                cv = colors[v[1]]
                if v[1] == value[1]:
                    self.board[(i, j-1)].remove(v)
                if value[0] > v[0]:
                    if cv > color:
                        self.board[(i, j-1)].remove(v)

        if j < self.dim-1:
            x = copy.deepcopy(self.board[(i, j+1)])
            for v in x:
                cv = colors[v[1]]
                if v[1] == value[1]:
                    self.board[(i, j+1)].remove(v)
                if value[0] > v[0]:
                    if cv > color:
                        self.board[(i, j+1)].remove(v)

    def select_next(self):
        m = 100000
        x = None
        for i in self.mrv.keys():
            if 1 < len(self.board[i]) < m:
                m = len(self.board[i])
                x = i
        return x

    def all_assigned(self):
        for i in self.mrv.keys():
            if len(self.board[i]) > 1:
                return False
        return True

    def empty_domain(self):
        for i in self.mrv.keys():
            if len(self.board[i]) == 0:
                return True
        return False

    def print_table(self):
        for i in range(self.dim):
            for j in range(self.dim):
                for k in self.board[(i, j)]:
                    print(str(k[0]) + k[1] + " ", end='')
            print()

    def assign(self):
        if self.all_assigned():
            return True
        chosen = self.select_next()
        # print(self.board[chosen])
        if chosen is not None:
            y = copy.deepcopy(self.board[chosen])
            for i in y:
                cpy = copy.deepcopy(self.board)
                cpy_m = copy.deepcopy(self.mrv)
                self.update_domain(chosen, i)
                self.board[chosen] = [i]
                # self.print_table()
                if not self.empty_domain():
                    if self.assign():
                        return True
                self.board = cpy
                self.mrv = cpy_m

        return False


if __name__ == '__main__':
    m, n = map(int, input().split())
    c = input().split()
    colors = {}
    for i in range(m):
        colors[c[i]] = m-i
    sudoku = Board(n)

    for i in range(n):
        s = input().split()
        for j in range(len(s)):
            num = []
            cc = []
            temp = []
            if s[j][0] == '*':
                num = [k for k in range(1, n+1)]
            else:
                num.append(int(s[j][0]))
            if s[j][1] == '#':
                cc = [k for k in c]
            else:
                cc.append(s[j][1])
            for x in num:
                for y in cc:
                    temp.append((x, y))
            sudoku.board[(i, j)] = temp
            sudoku.mrv[(i, j)] = len(temp)
    res = sudoku.assign()
    if res:
        sudoku.print_table()
    else:
        print("no valid solution!")


