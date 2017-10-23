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
        self.EXEC = [self.U, self.U_, self.U2, self.R, self.R_, self.R2]
        self.EXEC_NAME = ["U","U'","U2","R","R'","R2"]
                
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