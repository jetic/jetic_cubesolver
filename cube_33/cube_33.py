class CubeSolver33:    
    def __init__(self, state = None):
        self.FINAL = []
        for i in xrange(12):
            self.FINAL.append([i+1, 0])
        for i in xrange(8):
            self.FINAL.append([i+13, 0])
        self.STR_FINAL = str(self.FINAL)
            
        if (state):
            self.STATE = state
        else:
            self.STATE = [[x[0], x[1]] for x in self.FINAL]
        self.STR_STATE = str(self.STATE)
        
        self.U = [[1,2,0],[2,3,0],[3,4,0],[4,1,0],[13,14,0],[14,15,0],[15,16,0],[16,13,0]]
        self.U_ = [[x[1], x[0], -x[2]] for x in self.U]
        self.U2 = [[1,3,0],[2,4,0],[3,1,0],[4,2,0],[13,15,0],[14,16,0],[15,13,0],[16,14,0]]
        self.R = [[4,11,0],[11,8,0],[8,12,0],[12,4,0],[16,15,-1],[15,19,1],[19,20,-1],[20,16,1]]
        self.R_ = [[x[1], x[0], -x[2]] for x in self.R]
        self.R2 = [[4,8,0],[11,12,0],[8,4,0],[12,11,0],[16,19,0],[15,20,0],[19,16,0],[20,15,0]]
        self.F = [[1,12,1],[12,5,1],[5,9,1],[9,1,1],[13,16,-1],[16,20,1],[20,17,-1],[17,13,1]]
        self.F_ = [[x[1], x[0], -x[2]] for x in self.F]
        self.F2 = [[1,5,0],[12,9,0],[5,1,0],[9,12,0],[13,20,0],[16,17,0],[20,13,0],[17,16,0]]
        self.D = [[5,8,0],[8,7,0],[7,6,0],[6,5,0],[17,20,0],[20,19,0],[19,18,0],[18,17,0]]
        self.D_ = [[x[1], x[0], -x[2]] for x in self.D]
        self.D2 = [[5,7,0],[8,6,0],[7,5,0],[6,8,0],[17,19,0],[20,18,0],[19,17,0],[18,20,0]]
        self.L = [[2,9,0],[9,6,0],[6,10,0],[10,2,0],[13,17,1],[17,18,-1],[18,14,1],[14,13,-1]]
        self.L_ = [[x[1], x[0], -x[2]] for x in self.L]
        self.L2 = [[2,6,0],[9,10,0],[6,2,0],[10,9,0],[13,18,0],[17,14,0],[18,13,0],[14,17,0]]
        self.B = [[3,10,1],[10,7,1],[7,11,1],[11,3,1],[14,20,1],[20,19,-1],[19,15,1],[15,14,-1]]
        self.B_ = [[x[1], x[0], -x[2]] for x in self.B]
        self.B2 = [[3,7,0],[10,11,0],[7,3,0],[11,10,0],[14,19,0],[20,15,0],[19,14,0],[15,20,0]]
        self.EXEC = [self.U, self.U_, self.U2, self.R, self.R_, self.R2, self.F, self.F_, self.F2, self.D, self.D_, self.D2, self.L, self.L_, self.L2, self.B, self.B_, self.B2]
        self.EXEC_NAME = ["U","U'","U2","R","R'","R2","F","F'","F2","D","D'","D2","L","L'","L2","B","B'","B2"]
                
    def solve(self):
        self.OLD = {}
        self.OLD[self.STR_STATE] = True
        self.NOW = {}
        self.NOW[self.STR_STATE] = ""
        if (self.STR_STATE != self.STR_FINAL):
            solved = False
        else:
            return ""
        depth = 0
        while (not solved):
#        while (not solved and depth < 2):
            depth += 1
            print "In depth", depth
            now = {}
            for (k, v) in self.NOW.items():
#                print k,v
                for exec_id in xrange(len(self.EXEC)):
                    current_state = eval(k)
                    next_state = self.action(current_state, exec_id)
                    str_next_state = str(next_state)
                    if (str_next_state in self.OLD):
                        continue
                    else:
                        now[str_next_state] = v + self.EXEC_NAME[exec_id]
                    if (str_next_state == self.STR_FINAL):
                        solved = True
                        return now[str_next_state]
                self.OLD[k] = True
            self.NOW = now
            
    def action(self, state1, exec_id):
        state2 = [[x[0], x[1]] for x in state1]
        for x in self.EXEC[exec_id]:
            b1, b2, direction = x[0], x[1], x[2]
            state2[b2-1][0] = state1[b1-1][0]
            if (b1 <= 12): # edge
                if (direction == 0):
                    state2[b2-1][1] = state1[b1-1][1]
                else:
                    state2[b2-1][1] = 1 - state1[b1-1][1]
            else: # corner
                if (direction == 0):
                    state2[b2-1][1] = state1[b1-1][1]
                else:
                    new_direction = state1[b1-1][1] + direction
                    if (new_direction < -1):
                        new_direction = 1
                    if (new_direction > 1):
                        new_direction = -1
                    state2[b2-1][1] = new_direction
        return state2