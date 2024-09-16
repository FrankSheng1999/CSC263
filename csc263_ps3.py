'''
CSC263 Winter 2022
Problem Set 3 Starter Code
University of Toronto Mississauga
'''


# Do NOT add any "import" statements

class ve:
    def __init__(self, easier_ve):
        self.eas_ve = easier_ve
        self.start_time = 0
        self.finish_time = 0
        self.color = 'white'

    def __repr__(self):
        return str(self.eas_ve) + ' ' + self.color + ' ' + str(self.start_time) + ' ' + str(self.finish_time)


class easier_ve:
    def __init__(self, statement: int, boolean: bool):
        self.statement = statement
        self.bool = boolean

    def __repr__(self):
        return str(self.statement) + ' ' + str(self.bool)


class Graph:
    def __init__(self, statements: list):
        num = len(statements)
        self.ves = dict()
        self.ves_list = []
        for i in range(num):
            new_1 = easier_ve(i + 1, True)
            new_2 = easier_ve(i + 1, False)
            statement = statements[i]
            a = int(statement.split(' is ')[0][-1])
            b = (statement.split(' is ')[1])
            if b == 'FALSE':
                b = False
            else:
                b = True
            neighbour_1 = ve(easier_ve(a, b))
            neighbour_2 = ve(easier_ve(a, not b))
            self.ves[new_1] = neighbour_1
            self.ves[new_2] = neighbour_2
        for i in self.ves.values():
            self.ves_list.append(i)
        self.time = 0
        self.paradox = []

    def find_key(self, v: easier_ve):
        a = v.statement
        b = v.bool
        for key in self.ves.keys():
            if key.bool == b:
                if key.statement == a:
                    return key

    def dfs_visit(self, v: ve):
        v.color = 'gray'
        self.time += 1
        v.start_time = self.time
        c = self.find_key(v.eas_ve)
        if self.ves[c].color == 'white':
            self.dfs_visit(self.ves[c])
        v.color = 'black'
        self.time += 1
        v.finish_time = self.time

    def dfs(self):
        for v in self.ves_list:
            if v.color == 'white':
                self.dfs_visit(v)

    def paradox_adding(self):
        i = 0
        while i < len(self.ves_list):
            a = self.ves_list[i]
            b = self.ves_list[i + 1]
            if self.ves.get(a.eas_ve) in self.paradox:
                self.paradox += [a, b]
            elif (a.start_time < b.start_time) & (a.finish_time > b.finish_time):
                self.paradox += [a, b]
            elif (a.start_time > b.start_time) & (a.finish_time < b.finish_time):
                self.paradox += [a, b]
            i = i + 2


def detect_paradox(statements: list):
    """
  Given a list of statements of the form "Statement {X} is {TRUE/FALSE}",
  identify the set of paradoxical statement.
  """
    a = []
    detect_graph = Graph(statements)
    detect_graph.dfs()
    detect_graph.paradox_adding()
    b = detect_graph.paradox
    for v in b:
        if v.eas_ve.statement not in a:
            a = a + [v.eas_ve.statement]
    return a


# You may add additional test case below. HOWEVER, your code must
# compile and be runnable in order to earn any credit for correctness.

if __name__ == '__main__':
    # a small test case
    paradoxes = detect_paradox(['Statement 2 is FALSE',
                                'Statement 1 is TRUE',
                                'Statement 3 is TRUE'])
    assert set(paradoxes) == set([1, 2])
    paradoxes = detect_paradox(['Statement 3 is FALSE',
                                'Statement 3 is FALSE',
                                'Statement 4 is FALSE',
                                'Statement 4 is TRUE'])
    assert set(paradoxes) == set([])
    paradoxes = detect_paradox(['Statement 2 is FALSE',
                                'Statement 1 is TRUE',
                                'Statement 3 is FALSE'])
    assert set(paradoxes) == set([1, 2, 3])
