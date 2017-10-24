from cube_33 import CubeSolver33

def test1():
    state = []
    for i in xrange(12):
        state.append([i+1, 0])
    for i in xrange(8):
        state.append([i+13, 0])
    state[0][0] = 2
    state[1][0] = 1
    state[2][0] = 4
    state[3][0] = 3
    return state

def test2():
    state = []
    for i in xrange(12):
        state.append([i+1, 0])
    for i in xrange(8):
        state.append([i+13, 0])
    X = map(int, "6 3 4 5 7 1 2 8 9 11 12 10".split())
    for i in xrange(12):
        state[i][0] = X[i]
    X = map(int, "1 3 6 8 7 4 5 2".split())
    for i in xrange(8):
        state[i+12][0] = X[i] + 12
    return state

def main():
    state = test2()
    print "Start state: ", state
    Solver = CubeSolver33(state)
    result = Solver.solve()
    print "=========================="
    print "Solution: ", result
    
main()