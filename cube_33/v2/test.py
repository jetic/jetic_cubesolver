from cube_33 import CubeSolver33

def main():
#    state = test2()
#    print "Start state: ", state
    Solver = CubeSolver33()
    Solver.generate_corner_pos_table("corner_pos.jcs")
    
main()