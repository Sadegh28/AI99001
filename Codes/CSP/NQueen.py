class nqueen_csp: 
    def __init__(self, q_num): 
        #q_num: number of queens
        self.size = q_num
    
    def check_conflict(self,assignment):   

        #check for duplicate columns
        a = [i for i in assignment if i!= -1]
        a_set = set(a)
        if len(a) != len(a_set):
            return True
        
        #Diagonal check
        for r in range(self.size): 
            if assignment[r] == -1: 
                continue
            for k in range(1,self.size-r):
                if  (assignment[r+k] == assignment[r]+k) or (assignment[r+k] == assignment[r]-k): 
                    return True
        return False
    
    def goal_test(self, assignment): 
        a = [i for i in assignment if i == -1]
        if (self.check_conflict(assignment) != True and len(a) == 0):
            return True
        return False

    def Backtracking(self): 
        initial_assignment = [-1 for i in range(self.size)]
        return self.Recursive_Backtracking(initial_assignment)

    def Recursive_Backtracking(self, assignment): 
        #print(assignment)
        if(self.goal_test(assignment)): 
            return assignment
        
        #assignment in order 
        #todo: you can modify this part to select another row or value for assignment
        for i in range(self.size): 
            if assignment[i] == -1:
                for j in range(self.size): 
                    assignment[i] = j
                    if(self.check_conflict(assignment)): 
                        assignment[i]=-1
                        continue
                    if self.Recursive_Backtracking(assignment) is not "failure": 
                        return assignment
                    assignment[i] = -1
        return "failure"

   

   

            
         

    
a = nqueen_csp(12)
print(a.Backtracking())