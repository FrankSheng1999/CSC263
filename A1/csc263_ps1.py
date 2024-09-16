'''
CSC263 Winter 2021
Problem Set 1 Starter Code
University of Toronto Mississauga
'''


class Heap:
    

    def __init__(self):
        self.n = 0
        self.list_a = ['']  # a maximum heap
        self.list_b = ['']  # a minimum heap
        self.length_of_a = len(self.list_a) - 1
        self.length_of_b = len(self.list_b) - 1

    def insert(self, i):
        self.n += 1
        c = round(self.n * 0.618)
        d = self.n - c
        if self.n == 1:
            insert(self.list_b, i)
        else:
            root_note = self.list_b[1]
            if root_note < i:
                insert_large(self.list_a, i)
                if self.length_of_a > d:
                    minimum = remove_large(self.list_a)
                    insert(self.list_b, minimum)
            else:
                insert(self.list_b, i)
                if self.length_of_b > c:
                    maximum = remove(self.list_b)
                    insert_large(self.list_a, maximum)

    def gold_rate(self):
        if self.n == 1:
            return self.list_b[1]
        return self.list_a[1]


# Do NOT add any "import" statements
def solve_gold_prospecting(commands: [str]):
    """
    Pre: commands is a list of commands
    Post: return list of get_min results
    >>> solve_gold_prospecting(['insert 10','get_gold','insert 5','insert 2','insert 8','get_gold','insert -5','get_gold'])
    [10, 8, 8]
    """
    gold_rate = []
    a = Heap()
    for c in commands:
        if c.startswith('insert'):
            b = int(c.split(' ')[1])
            a.insert(b)
        elif c == 'get_gold':
            gold_rate.append(a.gold_rate())
    return gold_rate


def switch(list_a: list, a: int, b: int):
    """
    >>> list_a = [1,2,3,4,5]
    >>> switch(list_a, 1, 3)
    >>> list_a
    [1,4,3,2,5]
    """
    c = list_a[a]
    d = list_a[b]
    list_a[a] = d
    list_a[b] = c


def rotate(self: list):
    """
    >>> list_a = ['', 1,3,2,0]
    >>> rotate(list_a)
    >>> list_a
    ['', 0, 1, 2, 3]
    """
    a = len(self) - 1
    stop = False
    while (a > 1) & (not stop):
        if self[a] <= self[a // 2]:
            switch(self, a, a // 2)
            a = a // 2
        else:
            stop = True


def rotate_large(self: list):
    """
    >>> list_a = ['', 1,3,2,0]
    >>> rotate(list_a)
    >>> list_a
    ['', 0, 1, 2, 3]
    """
    a = len(self) - 1
    stop = False
    while (a > 1) & (not stop):
        if self[a] >= self[a // 2]:
            switch(self, a, a // 2)
            a = a // 2
        else:
            stop = True


def rotate_high(self: list):
    a = 1
    stop = False
    while (a <= (len(self) - 1) // 2) & (not stop):
        if self[a] > self[a * 2]:
            switch(self, a, a * 2)
            a = a * 2
        else:
            stop = True


def rotate_high_large(self: list):
    a = 1
    stop = False
    while (a <= (len(self) - 1) // 2) & (not stop):
        if self[a] < self[a * 2]:
            switch(self, a, a * 2)
            a = a * 2
        else:
            stop = True


def insert(self: list, i: int):
    """
    >>> list_a = ['']
    >>> insert(list_a, 1)
    >>> list_a
    ['', 1]
    >>> insert(list_a, 3)
    >>> list_a
    ['', 1, 3]
    >>> insert(list_a, 2)
    >>> list_a
    ['', 1, 3, 2]
    >>> insert(list_a, 0)
    >>> list_a
    ['', 0, 1, 2, 3]
    """
    self.append(i)
    if len(self) == 2:
        return
    else:
        rotate(self)


def insert_large(self: list, i: int):
    self.append(i)
    if len(self) == 2:
        return
    else:
        rotate_large(self)


def remove(list_a: list):
    """
    >>> list_a = ['']
    >>> remove(list_a)
    >>> list_a
    ['']
    >>> insert(list_a, 1)
    >>> remove(list_a)
    1
    >>> list_a
    ['']
    >>> insert(list_a, 0)
    >>> insert(list_a, 1)
    >>> insert(list_a, 2)
    >>> insert(list_a, 3)
    >>> remove(list_a)
    0
    >>> list_a
    ['', 1, 2, 3]
    """
    if len(list_a) == 1:
        return
    elif len(list_a) == 2:
        return list_a.pop()
    else:
        switch(list_a, 1, len(list_a) - 1)
        a = list_a.pop()
        rotate_high(list_a)
        return a


def remove_large(list_a: list):
    if len(list_a) == 1:
        return
    elif len(list_a) == 2:
        return list_a.pop()
    else:
        switch(list_a, 1, len(list_a) - 1)
        a = list_a.pop()
        rotate_high_large(list_a)
        return a


# You may add additional test case below. HOWEVER, your code must
# compile and be runnable in order to earn any credit for correctness.
if __name__ == '__main__':
    # some small test cases
    # Case 1
    assert [10, 8, 8] == solve_gold_prospecting(
        ['insert 10',
         'get_gold',
         'insert 5',
         'insert 2',
         'insert 8',
         'get_gold',
         'insert -5',
         'get_gold',
         ])

