import random
from matplotlib import pyplot as plt
class nqueen_csp: 
    def __init__(self, q_num): 
        #q_num: number of queens
        self.size = q_num
    
    def initial_assignment(self): 
        assignment = [random.randrange(self.size) for i in range(self.size) ]
        return assignment

    def next_assignment(self,assignment): 
        best_neighbour = assignment.copy()
        for i in range(self.size): 
           
            neighbour = assignment.copy()
            neighbour[i] = random.randrange(self.size) 
            if(self.eval(neighbour) < self.eval(best_neighbour)):
                best_neighbour = neighbour
        return best_neighbour
    
    def eval(self,assignment): 
        #count the num of conflicts
        conflict_num = 0        
        #Diagonal check
        for r in range(self.size): 
            for k in range(1,self.size-r):
                if  (assignment[r+k] == assignment[r] or assignment[r+k] == assignment[r]+k) or (assignment[r+k] == assignment[r]-k): 
                    conflict_num = conflict_num + 1
        return conflict_num

    def search(self): 
        current = self.initial_assignment()
        print(current)
        while(True): 
            print(self.eval(current))
            next = self.next_assignment(current)
            if(self.eval(next) >= self.eval(current)): 
                break
            current = next
        return current



a = nqueen_csp(50)
print(a.search())

            
         

