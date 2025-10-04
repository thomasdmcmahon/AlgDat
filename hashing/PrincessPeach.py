"""Solution to Kattis problem 'Saving Princess Peach'"""
import sys

data = sys.stdin.read().strip().split()
N = int(data[0]) # total number of obstacles
Y = int(data[1]) # number of obstacles Mario says hes found
obstacles = set(list(map(int, data[2:]))) # the next m obstacles

def solution_builtin():
    # Solution using Pythons built in set and hashmap
    missed = 0
    got = 0
    for i in range(0, N):
        if i in obstacles:
            got += 1
            continue
        print(i)
        missed += 1

    print(f'Mario got {got} of the dangerous obstacles.')

def solution_own_implementation():
    # Solution implementing own hashmap structure
    # Simple hash table
    SIZE = N * 2
    table = [[] for _ in range(SIZE)]

    def insert(x):
        idx = x % SIZE
        if x not in table[idx]:
            table[idx].append(x)
    
    def contains(x):
        idx = x % SIZE
        return x in table[idx]
    
    # insert Mario's obstacles
    for x in obstacles:
        insert(x)
    
    got = 0
    for i in range(0, N):
        if contains(i):
            got += 1
        else:
            print(i)
    print(f"Mario got {got} of the dangerous obstacles.")

solution_own_implementation()
