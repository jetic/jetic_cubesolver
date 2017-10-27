from cube_33 import CubeSolver33

def main():
#    state = test2()
#    print "Start state: ", state
    Solver = CubeSolver33()
#    Solver.generate_table("corner_pos.jcs","corner","pos")
#    Solver.generate_table("corner_dir.jcs","corner","dir")
    Solver.generate_table("edge_dir.jcs","edge","dir")
    
main()