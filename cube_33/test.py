from cube_33 import CubeSolver33

def main():
    state = []
    for i in xrange(12):
        state.append([i+1, 0])
    for i in xrange(8):
        state.append([i+13, 0])
    state[0][0] = 4
    state[1][0] = 1
    state[3][0] = 2
#    state[0][0] = 2
#    state[1][0] = 3
#    state[2][0] = 4
#    state[3][0] = 1
#    state[12][0] = 14
#    state[13][0] = 15
#    state[14][0] = 16
#    state[15][0] = 13
    Solver = CubeSolver33(state)
    print Solver.solve()
    
main()